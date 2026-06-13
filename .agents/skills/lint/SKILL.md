---
name: lint
description: checks if code adheres to style guidelines and is free of common errors
---

# Skill Instructions

run `python -m ruff check --fix 2>&1`

fix all the reported errors and warnings with ruff, ensure there are no more errors, and then run

`python -m pytest`