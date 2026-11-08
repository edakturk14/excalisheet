# Excalisheet

Turn technical content into **simple visuals**.

Excalisheet takes a blog post, technical explainer, rough notes, public docs page, terms, images, or one concept and turns it into a clean visual.

> **If a detail is not necessary to understand the idea, leave it out.**

That is the main rule.

## Three modes

### Diagram

For one concept.

Examples:
- CPU vs GPU
- how a KV cache works
- what model routing does
- ChatGPT vs GPT

Output: editable `.excalidraw`.

### Cheat sheet

For a full blog post, technical explainer, or docs overview.

Excalisheet finds the main question, removes anything that does not help answer it, and reduces the source to the few sections needed to tell the story.

Output: editable `.excalidraw`.

### Banner

For an X header, social banner, hero image, or landscape visual.

Examples:
- make an X banner about inference
- turn this post into a banner
- make a banner from this docs page
- make a landscape banner using these terms: tokens, prefill, decode, KV cache
- make a banner using these images and the terms model routing, cost, speed

Output: finished landscape PNG.

The default banner format is 3:1 with one clear idea, minimal copy, and a clean developer-tool/editorial style.

## Inputs

You can give Excalisheet:

- pasted text
- rough notes
- a blog post
- a technical article
- a public docs URL
- a public webpage URL
- terms or phrases
- 1-3 images

Examples:

```text
@Excalisheet turn this post into a cheat sheet
```

```text
@Excalisheet make a diagram explaining KV cache
```

```text
@Excalisheet turn https://docs.weaveos.com/router/overview into a cheat sheet
```

```text
@Excalisheet make an X banner using these terms: model routing, cost, speed
```

## The design system

Excalisheet is deliberately restrained.

- short copy
- generous whitespace
- simple shapes
- one clear visual idea
- restrained colors
- no unnecessary decoration

No gradients, blobs, sparkles, robot brains, or generic AI-infographic styling unless explicitly requested.

The goal is not to make technical content look impressive.

The goal is to make it **easy to understand**.

## Principles

1. **Simple is better.**
2. Start with one idea.
3. Every element needs a reason to exist.
4. Prefer one short label over a paragraph.
5. Remove something if the story still works without it.
6. Never add jargon just because it exists in the source.
7. Never invent technical facts to make a visual cleaner.

## Usage

The core workflow lives at:

`skills/excalisheet/SKILL.md`

## Status

Early open-source release.

## License

MIT
