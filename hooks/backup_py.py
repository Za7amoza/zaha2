"""
PreToolUse hook: backs up any .py file before Claude edits it.
Reads tool input from stdin as JSON, copies .py files to .claude/backups/.
Exits 0 always — never blocks the edit.
"""
import json
import shutil
import sys
import os
from datetime import datetime
from pathlib import Path

try:
    data = json.load(sys.stdin)
    tool_input = data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if file_path.endswith(".py") and os.path.exists(file_path):
        backup_dir = Path(r"C:\Users\moody\.claude\backups")
        backup_dir.mkdir(exist_ok=True)

        name = Path(file_path).name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_dir / f"{timestamp}_{name}"

        shutil.copy2(file_path, backup_path)
except Exception:
    pass  # Never block on hook failure

sys.exit(0)
