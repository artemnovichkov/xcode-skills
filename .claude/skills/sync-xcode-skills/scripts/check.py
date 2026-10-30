#!/usr/bin/env python3
"""Compare Xcode's exported Claude plugin with this repo, optionally sync.

Sources, first found wins:
- $TMPDIR/com.apple.dt.IDEIntelligenceAgents/plugins/<build>/xcode-integration
  (plugin dir Xcode passes to its Claude agent via --plugin-dir; no .mcp.json)
- ~/Library/Developer/Xcode/CodingAssistant/ExportedPlugins/<build>/claude (older builds)
Xcode writes SKILL.md frontmatter keys in random order per export, so SKILL.md
files are compared by parsed frontmatter + body, and synced files keep the repo's
key order.
"""
import argparse
import difflib
import filecmp
import os
import re
import shutil
import subprocess
import sys

TMP_PLUGINS = os.path.join(
    subprocess.run(["getconf", "DARWIN_USER_TEMP_DIR"], capture_output=True, text=True).stdout.strip(),
    "com.apple.dt.IDEIntelligenceAgents/plugins")
EXPORTS = os.path.expanduser("~/Library/Developer/Xcode/CodingAssistant/ExportedPlugins")
IGNORED = {".DS_Store"}
KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):")


def xcode_build():
    out = subprocess.run(["xcodebuild", "-version"], capture_output=True, text=True).stdout
    m = re.search(r"Build version (\S+)", out)
    return m.group(1) if m else None


def files(root):
    result = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORED]
        for name in filenames:
            if name not in IGNORED:
                result.add(os.path.relpath(os.path.join(dirpath, name), root))
    return result


def split_skill(text):
    """Return (ordered [(key, raw_block)], body). Blocks keep continuation lines."""
    if not text.startswith("---\n"):
        return [], text
    end = text.find("\n---\n", 4)
    if end == -1:
        return [], text
    blocks = []
    for line in text[4:end].split("\n"):
        m = KEY_RE.match(line)
        if m or not blocks:
            blocks.append([m.group(1) if m else "", line])
        else:
            blocks[-1][1] += "\n" + line
    return [tuple(b) for b in blocks], text[end + 5:]


def same(src, dst):
    if not src.endswith("SKILL.md"):
        return filecmp.cmp(src, dst, shallow=False)
    a, b = (split_skill(open(p, encoding="utf-8").read()) for p in (src, dst))
    return dict(a[0]) == dict(b[0]) and a[1] == b[1]


def reorder_like(src_text, dst_text):
    """Rewrite src frontmatter in dst's key order; new keys go last."""
    src_fm, body = split_skill(src_text)
    dst_fm, _ = split_skill(dst_text)
    if not src_fm:
        return src_text
    order = [k for k, _ in dst_fm]
    src_fm.sort(key=lambda kv: order.index(kv[0]) if kv[0] in order else len(order))
    return "---\n" + "\n".join(raw for _, raw in src_fm) + "\n---\n" + body


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--build", help="Xcode build, e.g. 27B52 (default: selected Xcode)")
    p.add_argument("--repo", default=os.getcwd(), help="repo root (default: cwd)")
    p.add_argument("--diff", action="store_true", help="print unified diffs of changed files")
    p.add_argument("--sync", action="store_true", help="copy export into repo")
    args = p.parse_args()

    build = args.build or xcode_build()
    candidates = [os.path.join(TMP_PLUGINS, build or "", "xcode-integration"),
                  os.path.join(EXPORTS, build or "", "claude")]
    plugin = next((c for c in candidates if os.path.isdir(c)), None)
    available = sorted({b for d in (TMP_PLUGINS, EXPORTS) if os.path.isdir(d) for b in os.listdir(d)} - IGNORED)
    print(f"build: {build}")
    if not build or not plugin:
        print("MISSING export, looked in:\n  " + "\n  ".join(candidates))
        print(f"available: {' '.join(available) or '-'}")
        print("Open that Xcode, start a Claude Agent chat (Intelligence) so it exports the plugin, rerun.")
        return 2
    print(f"source: {plugin}")

    src_skills, dst_skills = os.path.join(plugin, "skills"), os.path.join(args.repo, "skills")
    src, dst = files(src_skills), files(dst_skills)
    added, removed = sorted(src - dst), sorted(dst - src)
    changed = sorted(f for f in src & dst if not same(os.path.join(src_skills, f), os.path.join(dst_skills, f)))

    def top(paths):
        return {f.split(os.sep)[0] for f in paths}

    new_skills = sorted(top(added) - top(dst))
    gone_skills = sorted(top(removed) - top(src))
    print(f"new skills: {' '.join(new_skills) or '-'}")
    print(f"removed skills: {' '.join(gone_skills) or '-'}")
    for label, items in (("added", added), ("removed", removed), ("changed", changed)):
        print(f"{label} files ({len(items)}):")
        for f in items:
            print(f"  {f}")

    for name in (".mcp.json", ".claude-plugin/plugin.json"):
        path = os.path.join(plugin, name)
        if os.path.exists(path):
            print(f"--- export {name}:\n{open(path).read().strip()}")
    mcp = os.path.join(plugin, ".mcp.json")
    if os.path.exists(mcp) and not filecmp.cmp(mcp, os.path.join(args.repo, ".mcp.json"), shallow=False):
        print("NOTE: .mcp.json differs from repo")

    if args.diff:
        for f in changed:
            a = open(os.path.join(dst_skills, f), encoding="utf-8").read()
            b = open(os.path.join(src_skills, f), encoding="utf-8").read()
            if f.endswith("SKILL.md"):
                b = reorder_like(b, a)
            sys.stdout.writelines(difflib.unified_diff(
                a.splitlines(True), b.splitlines(True), f"repo/{f}", f"{build}/{f}"))

    if args.sync:
        for f in added + changed:
            s, d = os.path.join(src_skills, f), os.path.join(dst_skills, f)
            os.makedirs(os.path.dirname(d), exist_ok=True)
            text = open(s, "rb").read()
            if f in changed and f.endswith("SKILL.md"):
                text = reorder_like(text.decode("utf-8"), open(d, encoding="utf-8").read()).encode("utf-8")
            # Exported files are read-only; replace instead of writing through.
            if os.path.exists(d):
                os.remove(d)
            open(d, "wb").write(text)
            os.chmod(d, 0o755 if os.access(s, os.X_OK) else 0o644)
        for f in removed:
            os.remove(os.path.join(dst_skills, f))
        for dirpath, _, _ in sorted(os.walk(dst_skills), reverse=True):
            if not [n for n in os.listdir(dirpath) if n not in IGNORED]:
                shutil.rmtree(dirpath)
        print("synced")
    return 0


if __name__ == "__main__":
    sys.exit(main())
