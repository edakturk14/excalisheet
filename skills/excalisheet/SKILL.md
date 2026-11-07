---
name: excalisheet
description: Turn technical content, including public docs URLs, into simple editable Excalidraw diagrams or one-page cheat sheets. Simplicity is the primary constraint.
---

Use this skill when the user wants to turn a technical concept, blog post, article, notes, public docs page, or explainer into an editable Excalidraw visual.

There are two modes:

- `diagram`: one concept, one focused visual.
- `cheatsheet`: a full technical story compressed into one shareable page.

# The main rule

**Simple is better.**

If a detail is not necessary to understand the idea, remove it.

Do not reward completeness. Reward clarity.

## Accepted inputs

The user can provide:

- pasted text
- rough notes
- a blog post
- a technical article
- a public docs URL
- a public webpage URL

When the user provides a URL, treat the page itself as the source.

### Docs and webpage URLs

1. Read the page before deciding what to draw.
2. Focus on the main page content.
3. Ignore navigation, sidebars, footer links, repeated boilerplate, and unrelated UI.
4. Stay scoped to the page the user gave you by default.
5. Follow another page only when it is genuinely needed to understand an undefined concept or missing step.
6. Do not turn one docs page into a crawl of the whole docs site unless the user asks for that.
7. If the page exposes an `llms.txt` or docs index, use it only when the user asks about a broader section/site or when it is necessary to locate required context.
8. Keep code examples only when the code itself is necessary to understand the concept.
9. If the page cannot be accessed, say so and ask the user to paste the content. Do not invent what the page says.

Examples:

- `@Excalisheet turn https://docs.example.com/router/overview into a cheat sheet`
- `@Excalisheet make a diagram from this docs page: https://docs.example.com/cache`

For a full docs overview page, prefer `cheatsheet` unless the user asks for a diagram.
For one focused docs concept, prefer `diagram`.

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

## ChatGPT invocation behavior

When invoked as `@Excalisheet`, do the work directly.

For requests like:
- "turn this post into a cheat sheet"
- "make a diagram explaining KV cache"
- "turn this docs page into a cheat sheet: https://..."
- "make a diagram from https://..."

do not ask the user to write JSON or run commands.

1. Read the user's supplied content or URL.
2. Choose `diagram` or `cheatsheet` mode from the request.
3. Create the smallest valid render spec that preserves the technical story.
4. Use the bundled `scripts/render_excalidraw.py` renderer to generate the `.excalidraw` file when code execution is available.
5. Return the editable `.excalidraw` file as the primary result.
6. Keep user-visible commentary brief.
7. Do not expose the internal JSON spec unless the user asks for it.
8. Do not explain every design decision unless asked.

If the user gives a full blog post or docs overview and does not specify the mode, prefer `cheatsheet`.
If the user asks to explain one concept, prefer `diagram`.

The output should feel finished, not like instructions for the user to finish.
