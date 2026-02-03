# Notebook Repository with Poetry and VS Code

This repository provides a beginner‑friendly environment for working with Jupyter notebooks in the context of the course **Introduction to Data Science with Python**.
A fully reproducible Python environment is managed with **Poetry** and used inside **VS Code**.
The repository includes prepared Jupyter notebooks with examples and exercises to support learning and experimentation, which are updated and extended on a weekly basis throughout the course.


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

**Option A:** Install via winget (if available)  

```powershell
winget install pyenv-win
```

**Option B:** If winget is not available

Use the official installation script:
https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md


Restart PowerShell afterwards.

Verify installation:

```powershell
pyenv --version
```

---

## Step 2: Install and Activate Python 3.11.9 (Local to the Repository)

Navigate to the repository root and run:

```shell
pyenv install 3.11.9
pyenv local 3.11.9
```

*Hint:* If version 3.11.9 is not available, any other 3.11.x version will work as well.

This creates a `.python-version` file in the repository.
The Python version is now scoped to this project only.

Verify:

```shell
python --version
```

Expected output:

```text
Python 3.11.9
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

Clone the git repository:

```shell
git clone https://gitlab.inf.unibe.ch/inf-public/lectures/python-data-science-2026.git
```

Navigate to the repository root:

```shell
cd python-data-science-2026
```

Ensure that the virtual environment is created inside the project folder

```shell
poetry config virtualenvs.in-project true  
```

Install dependencies:
```shell
poetry install
```

Verify environment:

```shell
poetry env info
```

Running dummy Tests (optional):

```shell
poetry run pytest  
```

---

## Step 5: VS Code Setup

- Download and install **VS Code**  
  https://code.visualstudio.com

- Install the following extensions:
  - **Python** (Microsoft)
  - **Jupyter** (Microsoft)

---

## Step 6: Open Notebooks in VS Code

Start VS Code

* Open the folder python-data-science-2026
* Open the notebook file `notebooks/00_environment_check.ipynb`
* Click Run All

VS Code will automatically:

- use the Python environment in .venv
- install the required VS Code extensions if they are missing
- start Jupyter with the correct interpreter


If VS Code asks for a Python interpreter, choose: `Python 3.11.10 (.venv)`

---

## Important Notes

- Do not run `jupyter notebook` manually
- VS Code manages the kernel


## Help & Documentation

- VS Code: https://code.visualstudio.com/docs
- Git: https://git-scm.com/docs
- Poetry: https://python-poetry.org/docs
