# Excalisheet

Turn technical content into **simple, editable Excalidraw visuals**.

Excalisheet takes a blog post, technical explainer, rough notes, or one concept and turns it into an editable `.excalidraw` file.

> **If a detail is not necessary to understand the idea, leave it out.**

That is the main rule.

## Two modes

### Diagram

For one concept.

Examples:
- CPU vs GPU
- how a KV cache works
- what model routing does
- ChatGPT vs GPT
- a request flowing through a system

The output is one focused Excalidraw diagram.

### Cheat sheet

For a full blog post or technical explainer.

Excalisheet finds the main question, removes anything that does not help answer it, reduces the source to the few sections needed to tell the story, and ends with a short **In short** flow.

The output is one shareable, editable Excalidraw cheat sheet.

## The design system

Excalisheet is deliberately restrained.

- Excalidraw / Virgil font
- white canvas
- graphite text
- thin gray borders
- one accent color
- short copy
- generous whitespace
- simple boxes and arrows

No gradients. No blobs. No sparkles. No robot brains. No decorative complexity.

The goal is not to make technical content look impressive.

The goal is to make it **easy to understand**.

## How it works

```text
source content
      ↓
find the one question
      ↓
remove anything unnecessary
      ↓
choose the simplest visual structure
      ↓
build a small JSON spec
      ↓
render an editable .excalidraw file
```

## Principles

1. **Simple is better.**
2. Start with one question.
3. Every section needs a reason to exist.
4. Each section should make the next one feel necessary.
5. Prefer one short label over a paragraph.
6. Prefer one arrow over an explanation of the arrow.
7. Remove a section if the story still works without it.
8. Never add jargon just because it exists in the source.
9. Never invent technical facts to make the visual cleaner.
10. The editable Excalidraw file is the primary output.

## Usage

The core workflow lives at:

`skills/excalisheet/SKILL.md`

Render the included example:

```bash
python skills/excalisheet/scripts/render_excalidraw.py \
  skills/excalisheet/examples/chatgpt-inference.json \
  chatgpt-inference.excalidraw
```

## Project structure

```text
excalisheet/
├── README.md
├── LICENSE
├── plugin.json
├── skills/
│   └── excalisheet/
│       ├── SKILL.md
│       ├── references/
│       │   ├── style-guide.md
│       │   ├── diagram-mode.md
│       │   ├── cheatsheet-mode.md
│       │   └── spec-schema.md
│       ├── scripts/
│       │   └── render_excalidraw.py
│       └── examples/
│           └── chatgpt-inference.json
└── docs/
    ├── diagram.md
    └── cheatsheet.md
```

## Status

Early open-source release. v0.1 intentionally focuses on the workflow and visual system before adding a UI.

## License

MIT
