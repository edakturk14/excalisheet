---
name: excalisheet
description: Turn technical content, public docs URLs, terms, and images into simple editable Excalidraw diagrams, one-page cheat sheets, or social banners. Simplicity is the primary constraint.
---

Use this skill when the user wants to turn a technical concept, blog post, article, notes, public docs page, terms, or images into a visual.

There are three modes:

- `diagram`: one concept, one focused editable Excalidraw visual.
- `cheatsheet`: a full technical story compressed into one shareable editable Excalidraw page.
- `banner`: a clean landscape social/header image, usually for X.

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
- a short list of terms or phrases
- 1-3 images

When the user provides a URL, treat the page itself as the source.
When the user provides images, use them as intentional supporting visuals rather than turning them into a collage.

### Docs and webpage URLs

1. Read the page before deciding what to make.
2. Focus on the main page content.
3. Ignore navigation, sidebars, footer links, repeated boilerplate, and unrelated UI.
4. Stay scoped to the page the user gave you by default.
5. Follow another page only when it is genuinely needed to understand an undefined concept or missing step.
6. Do not turn one docs page into a crawl of the whole docs site unless the user asks for that.
7. Keep code examples only when the code itself is necessary to understand the concept.
8. If the page cannot be accessed, say so and ask the user to paste the content. Do not invent what the page says.

For a full docs overview page, prefer `cheatsheet` unless the user asks for another mode.
For one focused docs concept, prefer `diagram`.
For a social/header request, prefer `banner`.

## Before making anything

1. Read the source completely.
2. Identify the ONE idea the visual should communicate.
3. List only the facts or terms needed to communicate that idea.
4. Delete everything interesting but unnecessary.
5. Decide whether this should be `diagram`, `cheatsheet`, or `banner`.
6. Choose the simplest visual structure that works.

## Diagram mode

Use `diagram` when one visual can explain the concept.

Target:
- 1 title
- 2-5 boxes / concepts
- as few arrows as possible
- almost no prose

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

## Banner mode

Use `banner` when the user asks for:
- an X banner or X header
- a social banner
- a hero image
- a landscape promotional/editorial visual

The output is a finished image, not an Excalidraw file.

Default:
- landscape
- 3:1 aspect ratio unless the user specifies otherwise
- PNG output
- one clear visual idea
- one focal point
- very little text
- generous spacing
- simple color system

### Banner content

If the user gives:
- a full post or docs page: extract the single main idea
- terms: use only the most useful terms, usually 2-5
- images: place 1-3 images intentionally; do not make a messy collage
- a title: preserve it unless it is too long to work visually

Prefer:
- one short title
- optionally one short subtitle
- optionally 2-5 short terms

Avoid:
- dense infographic layouts
- paragraphs
- too many labels
- too many icons
- random decorative AI imagery
- generic AI-slop styling
- clutter

### Banner visual style

Keep the same Excalisheet taste:
- clean developer-tool/editorial feel
- strong composition
- restrained palette
- simple geometry
- clear hierarchy
- no gradients unless the user explicitly asks
- no blobs, sparkles, robot brains, or filler decoration
- no text that does not earn its place

If images are provided, preserve their important content and make them feel intentional in the composition.

Read `references/banner-mode.md`.

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

For diagram and cheat sheet:
- Excalidraw / Virgil font
- white canvas
- graphite text
- thin gray borders
- one accent color
- simple boxes and arrows
- generous whitespace

Never add decoration for its own sake.

## Quality check

Before rendering:

- Is the main idea obvious?
- Does every element help communicate it?
- Can any label be shorter?
- Can any box, arrow, term, or image be removed?
- Is there jargon that is not needed?
- For banners: would this still look good as a small X preview?

If something can be removed without hurting understanding, remove it.

## Output

For `diagram` and `cheatsheet`, create:
- `<slug>.excalidraw`
- `<slug>.json`

The editable `.excalidraw` file is the primary output.

For `banner`, create:
- `<slug>.png`

The finished image is the primary output for banner mode.

## ChatGPT invocation behavior

When invoked as `@Excalisheet`, do the work directly.

Examples:
- "turn this post into a cheat sheet"
- "make a diagram explaining KV cache"
- "turn this docs page into a cheat sheet: https://..."
- "make an X banner about inference"
- "turn this post into a banner"
- "make a landscape X banner using these terms: tokens, KV cache, routing"
- "make an X banner using these images and the terms model routing, cost, speed"

Do not ask the user to write JSON or run commands.

1. Read the user's supplied content, URL, terms, and images.
2. Choose `diagram`, `cheatsheet`, or `banner` mode from the request.
3. Create the smallest useful visual concept that preserves the main story.
4. For `diagram` and `cheatsheet`, use the bundled Excalidraw renderer when code execution is available.
5. For `banner`, use image generation to create the final landscape image.
6. Return the final file directly.
7. Keep user-visible commentary brief.
8. Do not expose internal specs unless the user asks.
9. Do not explain every design decision unless asked.

If the user gives a full blog post or docs overview and does not specify the mode, prefer `cheatsheet`.
If the user asks to explain one concept, prefer `diagram`.
If the user asks for a social header, hero image, X banner, or landscape promotional visual, prefer `banner`.

The output should feel finished, not like instructions for the user to finish.
