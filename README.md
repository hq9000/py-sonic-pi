# py-sonic-pi

Python wrapper for Sonic Pi.

## Prerequisites

- Python 3.8+
- [GNU Make](https://www.gnu.org/software/make/) — see below for Windows install

### Installing Make on Windows

```powershell
# Via Chocolatey (recommended)
choco install make

# Via scoop
scoop install make
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux

pip install -e ".[dev]"
```

## Available Commands

All commands are run via `make` from the project root:

| Command | Description |
|---|---|
| `make test` | Run all tests with pytest |
| `make lint` | Lint code with ruff |
| `make format` | Auto-format code with ruff |
| `make check` | Run lint + format (quick validation) |
| `make clean` | Remove build artifacts and cache directories |

## Examples

```bash
# Activate virtual environment first
.venv\Scripts\activate

# Run tests
make test

# Format and lint in one go
make check

# Clean up generated files
make clean
```
