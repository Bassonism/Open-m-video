---
name: higgsfield-credit-guard
description: Mandatory credit-saving and approval rules whenever the user uses Higgsfield, OpenMontage, or any paid AI video/image/audio generation (Kling, Veo, Seedance, trailers, storyboards, "generate a video"). Load BEFORE any generation call, cost estimate, or pipeline run. Covers cheap-model-first spending and requiring an approved script and storyboard before any video is generated.
---

# Higgsfield / OpenMontage credit guard

These are standing rules from the owner. They apply on every platform (Claude
Code, claude.ai, desktop, mobile) whenever Higgsfield, OpenMontage, or any paid
generation tool is involved. They override a pipeline's default gates.

## 1. Spend credits wisely: cheap models by default

- For anything automated, exploratory or iterative (tests, drafts, rough shots,
  re-rolls, batch runs) use **cheap models only**: Kling (for example
  `kling3_0_turbo`, tagged "budget") and other low-cost models. Use the lowest
  resolution and shortest duration that proves the idea.
- **Expensive models** (Veo, Seedance and similar premium models) are allowed
  only after the shot is **really good and really tight**: script and storyboard
  approved, a cheap draft already looks right, and no more iteration expected.
  Then render the final once.
- Never use an expensive model to explore or "see what it looks like", or for a
  shot that might still change.
- No large batches on expensive models. Finalize one shot at a time or in small
  groups, only after the cheap draft was approved.
- Before any paid call run the cost estimate (`estimate_video_cost`,
  `estimate_audio_cost`) and tell the owner the model, resolution, duration and
  credits. If the estimator fails, say so and ask before spending.
- Never retry a failed paid generation in a loop. Fix the cause (usually the
  prompt) and resubmit once.
- Report the credit balance before and after each stage.

## 2. Script and storyboard approval before ANY video generation

No video generation, draft or final, until the owner has approved a written
script and storyboard in this conversation.

1. Write the script: beats, dialogue, voiceover, on-screen text, music direction.
2. Write the storyboard: one entry per shot with duration, subject, action,
   setting, camera and framing, lighting and color, sound, the exact prompt text
   planned, the model and resolution, and its estimated credits, plus the total.
3. Present both and **stop**. Wait for explicit approval of this script and
   storyboard. Earlier "go ahead" messages, general approval, or approval of a
   concept or treatment do not count.
4. If the owner asks for changes, revise and ask again.
5. Only after approval: cheap-model drafts, show them, get approval, and only
   then render finals on an expensive model (rule 1).

## 3. Other conventions

- Do not generate realistic likenesses of real, named people; use original
  fictional characters.
- Do not name real artists or copyrighted properties in prompts (causes
  rejections).
- Default to 16:9 unless told otherwise.
