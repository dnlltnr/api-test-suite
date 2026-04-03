
# API Test Suite - Users


## Description
This project contains automated tests for a User API.
Its focused on validating API behavior and detecting potential issues.

- Note: The API used (jsonplaceholder.typicode.com) is a fake API and does not validate input data.

---

## Project Structure
```
api-test-suite/
├── api/
│   ├── __init__.py
│   └── user_api.py
├── tests/
│   └── test_users.py
├── README.md
├── requirements.txt
└── .gitignore
```
---

## What is tested
- Create user (valid data)
- Create user with invalid data
- API behavior with edge cases
- GET users endpoint

---

## Tech stack
- Python
- pytest
- requests

---

## How to run
1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run tests:

```bash
python -m pytest
```
