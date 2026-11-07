# Spec schema

Excalisheet accepts one JSON spec.

## Cheat sheet

```json
{
  "mode": "cheatsheet",
  "title": "What happens after you hit send on ChatGPT?",
  "subtitle": "A simple look at the infrastructure from prompt to answer.",
  "accent": "#7C5CFC",
  "sections": [
    {
      "number": "01",
      "title": "ChatGPT ≠ GPT",
      "why": "The app and model are different things.",
      "layout": "compare",
      "data": {
        "left": {
          "title": "ChatGPT = app",
          "body": ["Chat interface", "Conversation history"]
        },
        "right": {
          "title": "GPT = model",
          "body": ["Learned weights"]
        }
      }
    }
  ],
  "summary": [
    "App prepares request",
    "Routing picks a server",
    "Input becomes tokens",
    "GPU processes it",
    "Answer streams back"
  ]
}
```

## Diagram

```json
{
  "mode": "diagram",
  "title": "ChatGPT is not the model",
  "accent": "#7C5CFC",
  "layout": "compare",
  "data": {
    "left": {
      "title": "ChatGPT = app",
      "body": ["Chat interface", "Conversation history"]
    },
    "right": {
      "title": "GPT = model",
      "body": ["Learned weights"]
    }
  }
}
```

## Layouts

### compare

Two concepts side by side.

```json
{
  "left": {"title": "A", "body": ["..."]},
  "right": {"title": "B", "body": ["..."]}
}
```

### flow

A short sequence.

```json
{
  "steps": [
    {"title": "Input", "body": []},
    {"title": "Process", "body": ["Do the work"]},
    {"title": "Output", "body": []}
  ],
  "note": "Optional short note."
}
```

### route

One source routed to several destinations.

```json
{
  "source": "Your request",
  "router": {
    "title": "Routing",
    "body": ["Saved work", "Memory", "Load"]
  },
  "destinations": ["Server 1", "Server 2", "Server 3"],
  "note": "Optional short note."
}
```

### stack

A system and its components.

```json
{
  "stack_title": "SERVER",
  "stack_count": 3,
  "details": [
    {"title": "CPU + RAM", "body": ["Runs software"]},
    {"title": "GPU + VRAM", "body": ["Runs model work"]}
  ]
}
```

### tokens

Context becoming tokens.

```json
{
  "prompt": "Summarize my rent contract.",
  "context_title": "Input can include:",
  "context": ["Your question", "Document text", "Chat history"],
  "outputs": ["Input tokens", "Output tokens"]
}
```

### list

2-4 compact ideas.

```json
{
  "items": [
    {"title": "Compute", "body": "Calculations per second"},
    {"title": "Memory", "body": "How much data fits"}
  ]
}
```

## Constraints

- Cheat sheet: 4-6 sections maximum.
- Diagram: 2-5 concepts maximum.
- Keep titles short.
- Keep body lines short.
- Avoid prose where the geometry already explains the idea.
