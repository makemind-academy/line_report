# line-report

Five kinds of chart on one screen, every value fed from state; three of them point at the same hour.

Article: `five-charts-one-screen` (not yet published)

## What is here

- `line_report.mbd/` — the app as a folder of JSON: `manifest.json` and the pages under `ui/`. No build step.
- `captures/` — screenshots taken from AppPlayer by `verify.py`.
- `verify.py`, `verify.sh` — the check.

## Open it in AppPlayer

Install the folder `line_report.mbd`.

## Verify

```bash
bash verify.sh
```

Needs AppPlayer with the debug MCP on (see `tools/README.md`). The script builds what needs building, drives the player through the screens above, asserts the claim at the top of this file, and writes `captures/`.
