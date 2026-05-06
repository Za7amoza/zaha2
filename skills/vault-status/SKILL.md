---
name: vault-status
description: Quick health check of the RAMP Academy Obsidian vault — note count, fill status, transcript coverage, duplicate detection. Run anytime to see the current state without doing anything.
---

# Vault Status

Run a fast health check on the RAMP Academy Obsidian vault. Read-only — no changes made.

```bash
python -c "
import json, glob, os, re

VAULT = r'C:\Users\moody\OneDrive\Documents\Obsidian Vault\RAMP Academy'
TRANSCRIPTS = r'C:\Users\moody\ramp_transcripts\transcript_cache.json'

# Notes
all_notes = [f for f in glob.glob(VAULT + r'\**\*.md', recursive=True) if '00 - Index' not in f and 'Study Tracker' not in f]
dupes = [f for f in all_notes if '-za7amoza' in f]
clean_notes = [f for f in all_notes if '-za7amoza' not in f]

# Fill status
filled = []
unfilled = []
for note in clean_notes:
    try:
        content = open(note, encoding='utf-8').read()
        if 'TODO' in content or ('⚡ Practical' in content and len(content.split('⚡ Practical')[1].strip()) < 50):
            unfilled.append(note)
        else:
            filled.append(note)
    except: pass

# Transcripts
try:
    with open(TRANSCRIPTS, encoding='utf-8') as f:
        cache = json.load(f)
    transcript_count = len(cache)
except:
    transcript_count = 'ERROR - cache not found'

print('=' * 50)
print('RAMP VAULT STATUS')
print('=' * 50)
print(f'Notes (clean):     {len(clean_notes)}')
print(f'Duplicates:        {len(dupes)} {\"[NEEDS CLEANUP]\" if dupes else \"[OK]\"}')
print(f'Filled by AI:      {len(filled)}')
print(f'Unfilled:          {len(unfilled)}')
print(f'Transcripts:       {transcript_count}')
print(f'fill_vault ready:  {\"YES\" if not dupes else \"NO - clean dupes first\"}')
print('=' * 50)

if dupes:
    print(f'First duplicate: {os.path.basename(dupes[0])}')
if unfilled:
    print(f'First unfilled:  {os.path.basename(unfilled[0])}')
"
```

Report the output clearly. If duplicates exist, tell the user to run `/ramp-sync` first. If unfilled notes exist and no duplicates, tell the user fill_vault.py is ready to run.
