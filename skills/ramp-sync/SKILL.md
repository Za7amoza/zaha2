---
name: ramp-sync
description: Run the full RAMP Academy pipeline in order — reparse transcripts, rebuild Obsidian notes, report gaps, optionally fill vault. Use when rebuilding the vault, after adding new transcripts, or when notes feel out of sync.
---

# RAMP Sync

Run the RAMP Academy content pipeline in the correct order. All scripts live at `C:\Users\moody\`.

## Step 1 — Check for -za7amoza duplicates

Before anything else, check if duplicate files exist. They'll break fill_vault.py if present.

```bash
cd C:\Users\moody
python -c "
import glob, os
dupes = glob.glob(r'C:\Users\moody\OneDrive\Documents\Obsidian Vault\RAMP Academy\**\*-za7amoza.md', recursive=True)
print(f'{len(dupes)} duplicate files found')
for f in dupes[:5]: print(' ', f)
if len(dupes) > 5: print(f'  ... and {len(dupes)-5} more')
"
```

If duplicates found: ask user to confirm before deleting, then:
```bash
python -c "
import glob, os
dupes = glob.glob(r'C:\Users\moody\OneDrive\Documents\Obsidian Vault\RAMP Academy\**\*-za7amoza.md', recursive=True)
for f in dupes: os.remove(f)
print(f'Deleted {len(dupes)} duplicate files')
"
```

## Step 2 — Reparse transcripts

```bash
cd C:\Users\moody
PYTHONIOENCODING=utf-8 python reparse_transcripts.py
```

## Step 3 — Rebuild Obsidian notes

```bash
cd C:\Users\moody
PYTHONIOENCODING=utf-8 python skool_obsidian_episodes.py
```

## Step 4 — Report status

```bash
cd C:\Users\moody
python -c "
import json, glob, os

# Count notes
notes = glob.glob(r'C:\Users\moody\OneDrive\Documents\Obsidian Vault\RAMP Academy\**\*.md', recursive=True)
filled = [n for n in notes if '⚡' not in open(n, encoding='utf-8', errors='ignore').read()[:500] or 'TODO' not in open(n, encoding='utf-8', errors='ignore').read()[:500]]

# Count transcripts
with open(r'C:\Users\moody\ramp_transcripts\transcript_cache.json', encoding='utf-8') as f:
    cache = json.load(f)

dupes = glob.glob(r'C:\Users\moody\OneDrive\Documents\Obsidian Vault\RAMP Academy\**\*-za7amoza.md', recursive=True)

print(f'Notes: {len(notes)} total | {len(dupes)} duplicates remaining')
print(f'Transcripts: {len(cache)} in cache')
print(f'fill_vault.py: ready={len(dupes)==0}')
"
```

## Step 5 — Fill vault (optional, only if user confirms)

Only run if no duplicates and ANTHROPIC_API_KEY is set.

```bash
# Dry run first
cd C:\Users\moody
PYTHONIOENCODING=utf-8 python fill_vault.py

# Then ask user: "X notes would be filled. Run with --run? (~$1.50)"
# If yes:
PYTHONIOENCODING=utf-8 python fill_vault.py --run
```

Always do the dry run first and show the count before asking to proceed with `--run`.
