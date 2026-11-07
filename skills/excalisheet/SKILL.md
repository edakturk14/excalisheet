---
name: excalisheet
description: Turn technical content into simple editable Excalidraw diagrams or one-page cheat sheets. Simplicity is the primary constraint.
---

Use this skill when the user wants to turn a technical concept, blog post, article, notes, or explainer into an editable Excalidraw visual.

There are two modes:

- `diagram`: one concept, one focused visual.
- `cheatsheet`: a full technical story compressed into one shareable page.

# The main rule

**Simple is better.**

If a detail is not necessary to understand the idea, remove it.

Do not reward completeness. Reward clarity.

## Before drawing

1. Read the source completely.
2. Identify the ONE question the visual should answer.
3. List only the facts needed to answer that question.
4. Delete everything interesting but unnecessary.
5. Decide whether this should be a `diagram` or `cheatsheet`.
6. Choose the simplest layout that explains the idea.

## Diagram mode

Use `diagram` when one visual can explain the concept.

Target:
- 1 title
- 2-5 boxes / concepts
- as few arrows as possible
- almost no prose

Good:
- "ChatGPT = app"
- "GPT = model"

Bad:
- a paragraph explaining the difference inside each box

Read `references/diagram-mode.md`.

## Cheat sheet mode

Use `cheatsheet` for a full article or explainer.

Target:
- 4-6 sections maximum
- one question / idea per section
- each section must clearly lead to the next
- finish with an `In short` flow of 4-6 steps

If the story still works after removing a section, remove the section.

Read `references/cheatsheet-mode.md`.

## Writing

- Plain English.
- Short sentences.
- Short labels.
- Preserve the source author's voice where possible.
- Prefer concrete questions over category names.
- Define jargon only when necessary.
- Never introduce jargon just because it exists in the source.
- Never use promotional or generic AI language.
- Never invent technical facts.

Before finalizing each label, ask:

**Can this be shorter without losing meaning?**

If yes, shorten it.

## Visual system

Read `references/style-guide.md`.

Default:
- Excalidraw / Virgil font
- white canvas
- graphite text
- thin gray borders
- one accent color
- simple boxes and arrows
- generous whitespace

Never add decoration for its own sake.

No:
- gradients
- shadows
- blobs
- sparkles
- robot / brain imagery
- stock illustrations
- rainbow cards
- unnecessary icons

## Layouts

Prefer these primitives:

- `compare`: A vs B.
- `flow`: A → B → C.
- `route`: one request → one of several destinations.
- `stack`: zoom from a system into its components.
- `tokens`: source/context → tokens.
- `list`: 2-4 compact ideas.

Use the least complex layout that works.

## Quality check

Before rendering:

- Is the main question obvious?
- Does every section help answer it?
- Is there a clear reason for every section?
- Does each section lead naturally to the next?
- Can any label be shorter?
- Can any box be removed?
- Can any arrow be removed?
- Is there jargon that is not needed?
- Does the final summary match the actual story?

If something can be removed without hurting understanding, remove it.

## Output

Create:
- `<slug>.excalidraw`
- `<slug>.json`

The editable `.excalidraw` file is the primary output.
