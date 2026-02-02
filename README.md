# Notebook Repository with Poetry and VS Code

This repository is intended for beginners and is primarily used for working with Jupyter notebooks.
The Python environment is managed with **Poetry** and used inside **VS Code**.

## Goal

All students use the same Python version and the same dependencies.
Notebooks run reproducibly without manual environment setup.

---

## Requirements

- Windows 10/11, macOS, or Linux
- VS Code
- Git
- Internet connection

---

## Step 1: Install pyenv

### macOS

Install Homebrew (if not already installed)   
Homebrew is the package manager used to install pyenv on macOS.  
You can find the official installation instructions on the Homebrew website https://brew.sh/

```shell
brew install pyenv
```

Add the following lines to your shell configuration file (`~/.zshrc` or `~/.bashrc`):

```shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Restart the terminal or run `exec $SHELL`.

### Linux (Ubuntu/Debian)

```shell
sudo apt update
sudo apt install -y build-essential curl git
curl https://pyenv.run | bash
```

Add the following lines to `~/.bashrc`:

```shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Restart the terminal or run `exec $SHELL`.

### Windows

On Windows, use **pyenv-win**.

```powershell
winget install pyenv-win
```

Restart PowerShell.

Verify installation:

```powershell
pyenv --version
```

---

## Step 2: Install and Activate Python 3.11.10 (Local to the Repository)

Navigate to the repository root and run:

```shell
pyenv install 3.11.10
pyenv local 3.11.10
```

This creates a `.python-version` file in the repository.
The Python version is now scoped to this project only.

Verify:

```shell
python --version
```

Expected output:

```text
Python 3.11.10
```

---

## Step 3: Install Poetry 2.x

### macOS / Linux

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

Ensure Poetry is on PATH:

```shell
export PATH="$HOME/.local/bin:$PATH"
```


### Windows (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Ensure Poetry is on PATH:

```powershell
$env:Path += ";$env:APPDATA\Python\Scripts"
```

Verify:

```shell
poetry --version
```

Expected output (example):

```shell
Poetry (version 2.1.2)
```


---

## Step 4: Install the Repository

Navigate to the repository root:

```shell
cd <REPO-NAME>
```

Install dependencies:

```shell
poetry install
```

Verify environment:

```shell
poetry env info
```

---

## Step 5: Install Data Science Packages and Jupyter

```shell
poetry add numpy pandas matplotlib
poetry add jupyter ipykernel
```

Optional but common:

```shell
poetry add seaborn scikit-learn
```

Register the Poetry environment as a Jupyter kernel:

```shell
poetry run python -m ipykernel install \
  --user \
  --name poetry-notebooks \
  --display-name "Python (poetry-notebooks)"
```

---

## Step 6: VS Code Setup

Install extensions:

- Python (Microsoft)
- Jupyter (Microsoft)

Open the project:

```shell
code .
```

---

## Step 7: Select Jupyter Kernel

Open a notebook file (`.ipynb`) and select the kernel:

**Python (poetry-notebooks)**

Interpreter paths:

- macOS / Linux: `.venv/bin/python`
- Windows: `.venv\Scripts\python.exe`

---

## Working with Notebooks

- Notebooks are in `notebooks/`
- Shared code is in `src/`

Example import:

```python
from utils.helpers import my_function
```

---

## Running Tests (if applicable)

```shell
poetry run python -m pytest tests
```

---

## Important Notes

- Do not run `jupyter notebook` manually
- VS Code manages the kernel
- Do not use a global Python installation
- Do not change the Python version
- Always work inside the Poetry environment
- Commit `poetry.lock` and `.python-version`

