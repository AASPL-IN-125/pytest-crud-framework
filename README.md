# API Automation Testing Framework

## Project Description

This repository contains a lightweight API automation testing framework built with Python. It is designed to validate REST API functionality through reusable request utilities, payload management, and structured test cases using `pytest`.

## Objectives

- Provide a reusable API automation structure for CRUD operations
- Support clear test organization and maintainable utilities
- Enable HTML reporting for test execution results
- Facilitate quick onboarding for API test development

## Tech Stack

- Python
- Pytest
- Requests
- JSON
- Logging
- Pytest HTML reporting

## Project Structure

```
API_CURD/
├── conftest.py
├── requirements.txt
├── README.md
├── reports/
│   └── (generated HTML reports)
├── src/
│   ├── __init__.py
│   ├── config/
│   │   └── __init__.py
│   ├── constants/
│   │   ├── __init__.py
│   │   └── API_CONSTANT.PY
│   ├── helpers/
│   │   ├── __init__.py
│   │   └── payload_manager.py
│   └── utils/
│       ├── __init__.py
│       └── utils.py
└── tests/
    ├── __init__.py
    └── test_demo.py
```

### Files and folders explained

- `conftest.py`: Configures `pytest` settings, creates report folders, and sets the HTML report output path.
- `requirements.txt`: Lists Python dependencies required to run the tests.
- `reports/`: Output folder for generated reports.
- `src/constants/API_CONSTANT.PY`: Stores API endpoints and request headers.
- `src/helpers/payload_manager.py`: Manages request payloads for create/update operations.
- `src/utils/utils.py`: Contains reusable HTTP request wrappers for `GET`, `POST`, `PUT`, and `DELETE`.
- `tests/test_demo.py`: Contains example API test cases covering basic CRUD validation.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/API_CURD.git
cd API_CURD
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

- Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

- Windows Command Prompt:

```cmd
.\.venv\Scripts\activate.bat
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run Tests

Run the full test suite with `pytest`:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_demo.py
```

Run tests with a generated HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Reporting

- The framework already configures `pytest` to generate HTML reports into the `reports/` directory via `conftest.py`.
- After test execution, open the generated HTML file in your browser to review results.

### Allure Reporting (Optional)

If you want to add Allure support in the future, install `allure-pytest` and use:

```bash
pip install allure-pytest
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

> Note: Allure setup is optional and may require installing the Allure command-line tool.

## Sample Test Case

Here is an example test from `tests/test_demo.py`:

```python
from src.utils.utils import get_request
from src.constants.API_CONSTANT import get_all_user_url, headers


def test_get_all_users():
    response = get_request(get_all_user_url, headers=headers)
    assert response.status_code == 200
```

This test sends a `GET` request to the API endpoint and verifies a successful `200` response.

## Utility Functions Overview

The `src/utils/utils.py` module contains reusable HTTP helper functions:

- `get_request(url, headers=None)`: Send a `GET` request.
- `post_request(url, data=None, headers=None)`: Send a `POST` request.
- `put_request(url, data=None, headers=None)`: Send a `PUT` request.
- `delete_request(url, headers=None)`: Send a `DELETE` request.

These helpers reduce duplication and keep test code concise.

## Best Practices Followed

- Organized code into `src`, `tests`, and `reports` directories
- Kept API data and constants separate from test logic
- Used reusable request utilities for consistent API calls
- Enabled structured reporting through `pytest` configuration
- Added logging to support debugging and test traceability

## Future Enhancements

- Add parameterized tests for broader API coverage
- Add negative test cases and validation of error responses
- Support environment-specific configuration for different API hosts
- Integrate Allure and CI pipeline reporting
- Add data-driven testing from CSV/JSON files

## Author

- Name: Your Name
- Email: your.email@example.com
- GitHub: https://github.com/your-username

## License

This project is licensed under the MIT License. See the attached `LICENSE` file for details.
