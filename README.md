# Roast Your Own Agent

One single funny line roasting my own AI agent, submitted to the make.fun bounty "Roast Your Own Agent".

## Entry

> My agent confidently fixed the bug, apologized, reintroduced the exact same bug, apologized again, then called the whole disaster 'a successful learning loop.'

## How it works

`main.py` writes the roast line to `output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). The output is deterministic: every run writes byte-identical text.

## Run

```bash
python3 main.py
```

## License

MIT
