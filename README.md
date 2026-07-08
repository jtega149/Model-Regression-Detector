# Model Regression Detection System

A CI/CD-style pipeline that continuously tests any LLM-powered feature against a golden dataset whenever a prompt or model changes, detects quality regressions, and alerts your team via Slack before bad outputs reach users.

## Set Up

### Start Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate.bat

# MacOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create .env file in root directory for OpenAI key like so
.env
```bash
OPENAI_API_KEY=your_api_key
```


### Running tests
From root directory run the command (replace test_name with file name, exclude file extension ex: .py)
```bash
python -m tests.test_name
```
