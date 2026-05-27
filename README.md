# pytest-CRUD-Framework

## Project Description

This is a lightweight, production-ready **API automation testing framework** built with Python and pytest. It is designed to validate REST API functionality through reusable request utilities, comprehensive payload management, and well-structured test cases. The framework uses the **JSONPlaceholder API** as a mock backend for testing CRUD (Create, Read, Update, Delete) operations.

## Objectives

- ✅ Provide a reusable and modular API automation structure for CRUD operations
- ✅ Support clear test organization with maintainable utilities and helpers
- ✅ Enable comprehensive HTML and Allure reporting for test execution results
- ✅ Facilitate quick onboarding for API test development
- ✅ Include response verification utilities for validating status codes, headers, and JSON structures
- ✅ Support dynamic test data generation for realistic test scenarios

## Tech Stack & Dependencies

| Component | Purpose | Version |
|-----------|---------|---------|
| **Python** | Core language | 3.8+ |
| **pytest** | Test framework | 9.0.3 |
| **requests** | HTTP client library | 2.33.1 |
| **pytest-html** | HTML report generation | 4.2.0 |
| **pytest-xdist** | Parallel test execution | 3.8.0 |
| **allure-pytest** | Allure reporting | 2.15.3 |
| **python-dotenv** | Environment variable management | 1.2.2 |

## Project Structure

```
pytest-crud-framework/
├── conftest.py                          # pytest configuration & setup fixtures
├── requirements.txt                     # Python dependencies
├── README.md                            # Project documentation
├── Flow.md                              # Workflow & architecture diagram
├── reports/                             # Generated HTML & Allure reports
│   └── report_YYYY-MM-DD_HH-MM-SS.html
├── src/                                 # Source code - reusable modules
│   ├── __init__.py
│   ├── config/                          # Configuration module
│   │   └── __init__.py
│   ├── constants/
│   │   ├── __init__.py
│   │   └── API_CONSTANT.PY              # API endpoints, base URLs, headers
│   ├── helpers/
│   │   ├── __init__.py
│   │   ├── common_verifications.py      # Response verification utilities
│   │   └── payload_manager.py           # Test data & payload generation
│   └── utils/
│       ├── __init__.py
│       └── utils.py                     # HTTP request utilities (GET/POST/PUT/DELETE)
└── tests/
    ├── __init__.py
    └── test_demo.py                     # Demo test cases for CRUD operations
```

## Detailed Component Documentation

### 1. **conftest.py** - Test Configuration
```python
# Setup: pytest configuration, logging, and HTML report generation
# Features:
# - Automatic report generation with timestamps
# - Centralized logging configuration
# - Report location: D:\Automation\pytest-crud-framework\reports
```

**Key Functions:**
- `pytest_configure()`: Initializes pytest, sets up HTML report path and logging

---

### 2. **src/constants/API_CONSTANT.PY** - API Configuration
```python
base_url = "https://jsonplaceholder.typicode.com"
# Endpoints:
# - GET All Users: /users
# - GET User by ID: /users/1
# - POST User: /users
# - PUT User: /users/1
# - DELETE User: /users/1

headers = {'Content-Type': 'application/json'}
```

**Endpoints Overview:**
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | /users | Retrieve all users |
| GET | /users/1 | Retrieve specific user by ID |
| POST | /users | Create new user |
| PUT | /users/1 | Update existing user |
| DELETE | /users/1 | Delete user |

---

### 3. **src/helpers/common_verifications.py** - Response Verification
Provides functions to validate API responses:

**Available Functions:**
- `verify_status_code(response, expected_code)` - Verify HTTP status code
- `verify_header(response, header_name, expected_value=None)` - Verify response headers
- `verify_json_key(response, key, expected_value=None)` - Verify JSON response keys and values
- `verify_json_structure(response, expected_type)` - Validate JSON structure (list/dict)

**Example Usage:**
```python
response = get_request(url, headers)
verify_status_code(response, 200)
verify_json_key(response, 'id', 1)
verify_json_structure(response, 'dict')
```

---

### 4. **src/helpers/payload_manager.py** - Test Data Management
Manages test payloads and generates random test data.

**Predefined Payloads:**
```python
create_user_payload = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

update_user_payload = {
    "name": "Updated Name",
    "email": "updated@test.com"
}
```

**Dynamic Payload Generation:**
- `generate_user_payload()` - Generates random user data with random names and email addresses
  - Uses pool of 10 predefined names
  - Creates unique email addresses with random numbers
  - Returns dictionary with "name" and "email" keys

---

### 5. **src/utils/utils.py** - HTTP Request Utilities
Core utility functions for making HTTP requests.

**Available Functions:**
- `get_request(endpoint, headers=None)` - Send GET request
- `post_request(endpoint, data=None, headers=None)` - Send POST request
- `put_request(endpoint, data=None, headers=None)` - Send PUT request
- `delete_request(endpoint, headers=None)` - Send DELETE request

**Features:**
- Automatic logging for each request
- Pretty-printed JSON responses
- Returns `requests.Response` object for further validation

---

### 6. **tests/test_demo.py** - Test Cases
Comprehensive test suite demonstrating CRUD operations.

**Test Cases:**
1. **test_get_all_users()** - Verify GET all users returns 200 status
2. **test_get_user_by_id()** - Verify GET specific user returns 200 status
3. **test_create_user()** - Verify POST creates user with 201 status
4. **put_update_user()** - Verify PUT updates user with 200 status
5. **test_delete_user()** - Verify DELETE user returns 200 status

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps to Setup

1. **Clone/Navigate to Project Directory:**
   ```bash
   cd d:\Automation\pytest-crud-framework
   ```

2. **Create Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running Tests

### Run All Tests
```bash
pytest
```

### Run Tests with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run Tests with Verbose Output
```bash
pytest -v
```

### Run Specific Test
```bash
pytest tests/test_demo.py::test_get_all_users -v
```

### Run Tests in Parallel
```bash
pytest -n auto
```

### Generate Allure Report
```bash
pytest --alluredir=reports
allure serve reports
```

---

## Logging & Reports

### HTML Reports
- **Location**: `reports/report_YYYY-MM-DD_HH-MM-SS.html`
- **Features**: Test results, execution time, pass/fail status
- **Configuration**: Set in `conftest.py`

### Console Logging
- **Format**: `%(asctime)s - %(levelname)s - %(message)s`
- **Level**: INFO
- Logs all API requests and response statuses

---

## API Response Examples

### GET All Users Response (Status 200)
```json
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "email": "Sincere@april.biz",
    ...
  },
  ...
]
```

### GET User by ID Response (Status 200)
```json
{
  "id": 1,
  "name": "Leanne Graham",
  "email": "Sincere@april.biz",
  ...
}
```

### POST Create User Response (Status 201)
```json
{
  "id": 101,
  "name": "Generated Name",
  "email": "generated.email@yopmail.com"
}
```

---

## Key Features

- **Modular Design**: Separate concerns - constants, utilities, helpers, tests
- **Reusable Components**: All HTTP utilities and verifications can be imported
- **Dynamic Test Data**: Random payload generation for varied test scenarios
- **Comprehensive Logging**: Track all API interactions and responses
- **HTML Reporting**: Automatic test report generation with timestamps
- **Error Handling**: Robust logging for debugging failed tests
- **Parallel Execution**: Support for running tests concurrently

---

## Best Practices Used

✅ **DRY Principle** - Reusable utilities and helpers  
✅ **Clear Naming** - Descriptive function and file names  
✅ **Modular Structure** - Separation of concerns  
✅ **Comprehensive Logging** - Track all operations  
✅ **Data-Driven Testing** - Dynamic payload generation  
✅ **Standard Python Structure** - Follows pytest conventions  

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Import errors | Ensure all packages from requirements.txt are installed |
| Report not generated | Check write permissions in `reports/` directory |
| API endpoint unreachable | Verify internet connection and JSONPlaceholder API availability |
| Tests timeout | Increase timeout settings or check network connectivity |

---

## Future Enhancements

- [ ] Add environment configuration for multiple test environments
- [ ] Implement database validation tests
- [ ] Add API authentication (OAuth, JWT)
- [ ] Create custom fixtures for common test scenarios
- [ ] Add performance testing capabilities
- [ ] Integrate with CI/CD pipeline

---

## Contact & Support

For questions or issues, please refer to the project documentation or check the logs in generated reports.

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
