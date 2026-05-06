---
description: Watch a video (URL or local path). Downloads with yt-dlp, extracts frames with ffmpeg, transcribes from captions or Whisper, and answers questions about what's in the video.
argument-hint: <video-url-or-path> [question]
allowed-tools:
  - Bash
  - Read
---

# /watch — Claude watches a video

The scripts live at `C:/Users/moody/.claude/plugins/marketplaces/claude-video/scripts/`. On Windows, use `python` not `python3`.

Follow this pipeline with the user's arguments: $ARGUMENTS

## Step 0 — Setup preflight

```bash
python "C:/Users/moody/.claude/plugins/marketplaces/claude-video/scripts/setup.py" --check
```

On exit 0 → proceed silently. On non-zero:
- Exit 2: missing binaries → run `python "C:/Users/moody/.claude/plugins/marketplaces/claude-video/scripts/setup.py"`
- Exit 3: no Whisper API key → scaffold .env, ask user for key
- Exit 4: both → install then ask for key

Skip Step 0 on follow-up `/watch` calls within the same session.

## Step 1 — Parse input

Separate video source (URL or path) from any question. Example: `/watch https://youtu.be/abc what language?` → source = URL, question = "what language?"

## Step 2 — Run watch script

```bash
python "C:/Users/moody/.claude/plugins/marketplaces/claude-video/scripts/watch.py" "<source>"
```

Optional flags:
- `--start T` / `--end T` — focus on a section (SS, MM:SS, or HH:MM:SS)
- `--max-frames N` — lower frame cap (default auto-scales by duration, max 100)
- `--resolution W` — frame width in px (default 512; use 1024 only for on-screen text)
- `--fps F` — override auto-fps (capped at 2)
- `--no-whisper` — skip Whisper fallback (frames-only if no captions)
- `--whisper groq|openai` — force a specific Whisper backend

Frame budget by duration: ≤30s→30 frames, 30s-1min→40, 1-3min→60, 3-10min→80, >10min→100 (sparse).

For focused sections (user asks about a specific moment), pass `--start`/`--end` for denser frame extraction.

## Step 3 — Read every frame

The script prints frame paths. Use the Read tool on ALL frame paths (parallel tool calls). Frames are chronological with `t=MM:SS` timestamps.

## Step 4 — Answer

You have frames (visual) + transcript (spoken). If the user asked a question, answer citing timestamps. If not, summarize: structure, key moments, visuals, spoken content.

## Step 5 — Clean up

The script prints a working directory. Delete it with `rm -rf <dir>` unless the user might ask follow-ups.

## Transcription

1. Native captions (free, preferred) — yt-dlp pulls subs from the platform
2. Whisper API fallback — extracts audio, uploads to Groq (preferred) or OpenAI

Keys live in `~/.config/watch/.env`. Use `--no-whisper` to skip.

## Failure handling

- Download fails → report yt-dlp error plainly, don't retry
- No transcript → proceed frames-only, tell the user
- Long video warning → offer to re-run focused on a section
- Whisper fails → try the other backend, or proceed frames-only

## Token efficiency

~50-80k image tokens for 80 frames at 512px. Don't re-run the script for follow-up questions — answer from context. Only bump to `--resolution 1024` when necessary (4x token cost).
