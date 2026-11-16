# OpenMontage — Getting Started

Prepared in a cloud sandbox session. Upstream: https://github.com/OpenMontageInc/OpenMontage (AGPLv3).

## How it works (30 seconds)
You open the repo in an AI coding assistant (Claude Code, Cursor, Codex, ...) and describe a video.
The agent picks a pipeline from `pipeline_defs/`, runs preflight to see which tools/keys you have,
proposes concepts + cost, then executes stage by stage, pausing for your approval at each creative gate.
Rules the agent follows live in `AGENT_GUIDE.md`, `PROJECT_CONTEXT.md` and `skills/`.

## Install on your own machine
```bash
git clone https://github.com/OpenMontageInc/OpenMontage.git
cd OpenMontage
make setup        # venv, Python deps, Remotion npm deps, Piper, HyperFrames cache, .env
make preflight    # shows which tools are available
make demo         # renders zero-key demo videos
```
Prerequisites: Python 3.10+, FFmpeg, Node 22.23.4+ (see `.node-version`).
Then open the folder in Claude Code and prompt it.

## Status in the sandbox
| Item | Status |
|---|---|
| Clone + `make setup` | OK |
| HyperFrames runtime (`make hyperframes-doctor`) | OK |
| Remotion render (zero-key demo) | OK, 1080p/23s MP4 -> `samples/world-in-numbers.mp4` |
| Piper offline TTS | Installed, but voice model download blocked by sandbox network (works on a normal machine) |
| Image / video / TTS / music generation | Need API keys (none set) |

Sandbox-only workaround: Remotion could not download its own headless Chrome (blocked host), so I rendered with
`--browser-executable /opt/pw-browsers/chromium`. You will not need this on your machine.

## API keys — start free, add as needed (put in `.env`)
| Order | Key | Cost | Unlocks |
|---|---|---|---|
| 1 | `PEXELS_API_KEY`, `PIXABAY_API_KEY` | free | stock footage/images, Pixabay music |
| 2 | `GOOGLE_API_KEY` | free tier | TTS (700+ voices), Imagen |
| 3 | `ELEVENLABS_API_KEY` | free tier | premium TTS, music, SFX |
| 4 | Piper voice (`python -m piper.download_voices --download-dir ~/.piper/models en_US-lessac-medium`) | free | fully offline narration |
| 5 | `FAL_KEY` | ~$0.03/image, video per clip | FLUX images, Kling/Veo/MiniMax video |
| 6 | `OPENAI_API_KEY` | ~$0.05/image | GPT Image, OpenAI TTS |

Full list and pricing: `docs/PROVIDERS.md`. Keep keys out of git (`.env` is for local use only).

## Pipelines (`pipeline_defs/`)
animated-explainer, animation, avatar-spokesperson, character-animation, cinematic, clip-factory,
documentary-montage, hybrid, localization-dub, podcast-repurpose, screen-demo, talking-head.

## Starter prompts
- Zero keys: "Make a 30-second kinetic-typography piece about <topic> using HyperFrames/Remotion, no narration."
- Free keys (Pexels): "Make a 75-second documentary montage about city life in the rain. Real footage only, no narration, elegiac tone, with music."
- Paid: "Make a 60-second animated explainer about how neural networks learn."
- Reference: "Here's a YouTube Short I love: <url>. Make something like it, but about <topic>."

## Good to know
- Every production goes through a pipeline; don't ask the agent to call APIs ad hoc.
- The agent must announce provider/model/cost before paid calls and ask before changing them. Ask for a sample before a full run.
- Both Remotion and HyperFrames render engines are available; the agent will ask you to choose.
- Preview the live storyboard locally with `python -m backlot open`.
- Re-check capabilities any time: `make preflight`.
