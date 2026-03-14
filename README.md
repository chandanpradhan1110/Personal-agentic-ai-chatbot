# Project Setup Guide

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#project-setup-guide)

This guide provides step-by-step instructions to set up your project environment, including setting up a Python virtual environment using Pipenv, pip, or conda.

## Table of Contents

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#table-of-contents)

1. [Setting Up a Python Virtual Environment](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#setting-up-a-python-virtual-environment)
   * [Using Pipenv](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#using-pipenv)
   * [Using pip and venv](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#using-pip-and-venv)
   * [Using Conda](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#using-conda)
2. [Running the application](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#project-phases-and-python-commands)

## Setting Up a Python Virtual Environment

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#setting-up-a-python-virtual-environment)

### Using Pipenv

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#using-pipenv)

1. **Install Pipenv (if not already installed):**

```
pip install pipenv
```

2. **Install Dependencies with Pipenv:**

```
pipenv install
```

3. **Activate the Virtual Environment:**

```
pipenv shell
```

---

### Using `pip` and `venv`

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#using-pip-and-venv)

#### Create a Virtual Environment:

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#create-a-virtual-environment)

```
python -m venv venv
```

#### Activate the Virtual Environment:

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#activate-the-virtual-environment)

**macOS/Linux:**

```
source venv/bin/activate
```

**Windows:**

```
venv\Scripts\activate
```

#### Install Dependencies:

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#install-dependencies)

```
pip install -r requirements.txt
```

---

### Using Conda

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#using-conda)

#### Create a Conda Environment:

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#create-a-conda-environment)

```
conda create --name myenv python=3.11
```

#### Activate the Conda Environment:

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#activate-the-conda-environment)

```
conda activate myenv
```

#### Install Dependencies:

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#install-dependencies-1)

```
pip install -r requirements.txt
```

# Project Phases and Python Commands

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#project-phases-and-python-commands)

## Phase 1: Create AI Agent

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#phase-1-create-ai-agent)

```
python ai_agent.py
```

## Phase 2: Setup Backend with FastAPI

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#phase-2-setup-backend-with-fastapi)

```
python backend.py
```

## Phase 3: Setup Frontend with Streamlit

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#phase-3-setup-frontend-with-streamlit)

```
python frontend.py
```

## IMPORTANT

[](https://github.com/AIwithhassan/ai-agent-chatbot-with-fastapi/blob/main/Readme.md#important)

### Make sure backend python script is running in a separate terminal
