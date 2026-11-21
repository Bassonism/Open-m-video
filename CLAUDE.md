# Project rules: OpenMontage + Higgsfield

These are standing rules from the owner. Follow them in every session that uses
OpenMontage, Higgsfield, or any paid video/image/audio generation.

## 1. Spend credits wisely: cheap models by default

- For anything automated, exploratory, or iterative (tests, drafts, rough shots,
  re-rolls, batch runs), use **cheap models only**: Kling (e.g. `kling3_0_turbo`,
  tagged "budget") and other low-cost models. Prefer the lowest resolution and
  shortest duration that proves the idea.
- **Expensive models** (Veo, Seedance, and similar premium models) are allowed
  only after the shot is **really good and really tight**: the script, storyboard
  and prompt are approved, the cheap draft already looks right, and no further
  iteration is expected. Then render the final once.
- Do not use an expensive model for exploration, "to see what it looks like",
  or for shots that might change.
- Do not batch many expensive generations at once. Finalize a shot at a time
  or in small groups, after the cheap draft was approved.
- Before any paid call, run the cost estimate (`estimate_video_cost` /
  `estimate_audio_cost`), and tell the owner the model, resolution, duration and
  credits. If the estimator fails, say so and ask before spending.
- Never retry a failed paid generation in a loop. Fix the cause (usually the
  prompt) and resubmit once.
- Report the credit balance before and after each stage.

## 2. Script and storyboard approval before ANY video generation

No video generation, draft or final, until the owner has approved a written
**script and storyboard** in this conversation. This applies even if the
pipeline's default gates seem to allow it.

1. Write the script (beats, dialogue, voiceover, on-screen text, music direction).
2. Write the storyboard: one entry per shot with duration, subject, action,
   setting, camera and framing, lighting and color, sound, and the exact prompt
   text planned for the generator. Note which model and resolution each shot
   will use and its estimated credit cost, and the total.
3. Present both and **stop**. Wait for explicit approval of this script and
   storyboard. An earlier "go ahead", a general approval, or approval of a
   treatment or concept does not count.
4. If the owner requests changes, revise and ask again.
5. Only after approval: cheap-model drafts first, show them, get approval, and
   only then render finals on an expensive model (see rule 1).

## 3. Other conventions

- Real people: do not generate realistic likenesses of real, named people.
  Use original fictional characters.
- Prompts: avoid naming real artists or copyrighted properties; these trigger
  rejections.
- 16:9 unless told otherwise.
- Save outputs under `output/`. Commit and push only when asked (or when a
  stop hook requires it), and only to the session's designated branch.
