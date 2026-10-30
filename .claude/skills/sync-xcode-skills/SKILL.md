---
name: sync-xcode-skills
description: Check and sync this repo's skills/ against the Claude plugin exported by an installed Xcode build (e.g. 27B52). Use when a new Xcode/beta is installed, or asked to check, compare, update, or sync the Xcode skills.
metadata:
  internal: true
---

# Sync Xcode skills

Source of truth is the **plugin Xcode exports for the Claude agent**, not other copies. Script checks, first found wins:

```
# 27B52+: dir Xcode passes to its agent as --plugin-dir; no .mcp.json (MCP via --mcp-config)
$(getconf DARWIN_USER_TEMP_DIR)com.apple.dt.IDEIntelligenceAgents/plugins/<build>/xcode-integration/
# older builds
~/Library/Developer/Xcode/CodingAssistant/ExportedPlugins/<build>/claude/   # + .mcp.json
  .claude-plugin/plugin.json   # name: xcode-integration
  skills/<skill>/...
```

Tmp dirs of older builds get emptied by Xcode — only the current build is reliable there. If unsure where the plugin lives: `pgrep -lf "XcodeVersions/.*/claude"` and read its `--plugin-dir`.

Ignore `~/Library/Developer/Xcode/CodingAssistant/codex/skills/__xcode` (stale, e.g. still has `uikit-app-modernization`) and the flattened `*.packaged` / `*.idechatprompttemplate` files inside Xcode.app.

## Steps

1. Check (build defaults to `xcodebuild -version` of the selected Xcode; pass `--build` for another):
   ```bash
   python3 .claude/skills/sync-xcode-skills/scripts/check.py [--build 27B52]
   ```
   - Exit 2 = no export for that build. Xcode writes it only when a Claude Agent chat starts (a message sent) in that Xcode. Ask user to open one, then rerun. Don't reconstruct from Xcode.app.
   - Output: new/removed skills, added/removed/changed files, export `.mcp.json` + `plugin.json`.
2. Nothing changed → report "repo matches <build>" and stop.
3. Review: `--diff` prints unified diffs. Summarize per skill what changed (new sections, removed guidance, new references) — this goes into the commit message/README.
4. Sync only when user asks: `--sync`. Copies added/changed, deletes removed, keeps repo's frontmatter key order.
5. After sync, update by hand:
   - `README.md` skills table: add/remove rows for new/removed skills (one-line summary from SKILL.md description, same style as existing rows). Check plugin-dependent list in Install section (`device-interaction`, `translation`, ...) if a new skill uses Xcode MCP tools.
   - `.mcp.json`: match export if script reports `NOTE: .mcp.json differs`.
   - `.claude-plugin/marketplace.json`: bump `metadata.version` minor; update plugin `description` if skills added/removed.
6. Commit only when asked. Style: `Update skills for Xcode 27.2 (27B52), bump to 0.7.0`; mention added/removed skills.

## Gotchas

- Xcode emits SKILL.md frontmatter keys in random order per export. Script compares parsed frontmatter, so order-only differences are not changes. Never `cp -R` the export over the repo — it creates noisy diffs.
- Exported files are read-only (`r--r--r--`); script rewrites them as 644.
- `.DS_Store` ignored.
- Skill text references `xcode-integration:<skill>` (plugin name in Xcode). Keep verbatim — content is Apple's, unedited.
- Compare against older exports to see history between builds: `--build 27B48`.
