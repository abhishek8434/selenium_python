# CLYMB_AUTOMATION

## Overview
This project is a Selenium-based test automation framework written in Python. It uses pytest as the testing framework and is designed to test the functionality of the CLYMB application.

## Project Structure
The project is organized as follows:

```
|-- .github
|    |-- workflows
|        |-- build.yml
|-- assets
|    |-- style.css
|-- pages
|    |-- __pycache__
|    |-- admin_login.py
|    |-- login.py
|    |-- logout.py
|-- tests
|    |-- __pycache__
|    |-- __init__.py
|    |-- admin_first.py
|    |-- appreciation_check.py
|    |-- ask_for_help_form.py
|    |-- check_ask_for_help_in_admin.py
|    |-- clymb_appreciation_submit.py
|    |-- clymb_postiveflow_with_ifcondition.py
|    |-- clymb_reload_refresh_check.py
|    |-- clymb_test.py
|    |-- clymb.py
|    |-- grade_5.py
|    |-- wall_of_wonder.py
|-- utils
|    |-- __pycache__
|    |-- aftermood.py
|    |-- aftermoodchanges.py
|    |-- appreciation.py
|    |-- audio.py
|    |-- condition_for_negative_flow.py
|    |-- emotions_function.py
|    |-- locators.py
|    |-- locators_for_grade_5.py
|    |-- responsible_decison_making.py
|    |-- self_management.py
|    |-- social_awareness.py
|    |-- verify_ask_for_help_locator.py
|    |-- wall_of_wonder_locators.py
|-- .env
|-- .gitignore
|-- azure-pipelines-2.yml
|-- README.md
|-- Report.html
|-- requirements.txt

```

### Key Directories and Files
- **.github/workflows/**: Contains CI/CD workflow files, such as `build.yml`, for GitHub Actions.
- **assets/**: Holds static assets like CSS files.
- **pages/**: Includes page-specific Python scripts for handling login, logout, and admin login functionalities.
- **tests/**: Contains all the test scripts.
- **utils/**: Includes utility scripts, such as locators, helper functions, and other reusable components.
- **azure-pipelines-2.yml**: Azure Pipelines configuration file for CI/CD integration.
- **Report.html**: Generated test report.
- **requirements.txt**: Lists the Python dependencies required for this project.

---
## Setup Instructions

### Prerequisites
- Python 3.8 or higher installed on your system.
- `pip` (Python package installer) installed.
- Google Chrome or another supported browser
- ChromeDriver or the appropriate WebDriver for your browser

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running Tests

### To execute all tests:
```bash
pytest
```

### To execute a specific test file:
```bash
pytest tests/<test_file_name>.py
```
### To generate report:
```bash
pip instal pytest-html
```

### To generate a detailed report:
```bash
pytest --html=report.html --self-contained-html
```
### To generate a customized detailed report:
```bash
pytest --html=report.html --self-contained-html --metadata "Environment" "Production" --metadata "Tester" "Your Name"
```
### To open report
```bash
pytest start report.html
```
### To execute a specific test file to generate report :
```bash
pytest tests/<test_file_name>.py --html=report.html --self-contained-html --metadata "Environment" "Production" --metadata "Tester" "Your Name"
```

### Run Tests with Verbose Output
For detailed output during test execution:
```bash
pytest -v
```
### Run Tests with Specific Markers
If markers are used in the test suite, you can run tests with a specific marker:
```bash
pytest -m <marker_name>
```

---

## Environment Variables
Set the required environment variables by updating the `.env` file in the project root directory. These variables might include API keys, URLs, or other configurations specific to the tests.

---

## Key Features
- **Page Object Model (POM):** All web page interactions are encapsulated in the `pages` directory.
- **Reusable Utilities:** Commonly used functions and locators are located in the `utils` directory.
- **Environment Management:** Supports `.env` file for configurable variables.
- **Scalable Test Cases:** Organized in the `tests` directory, with dedicated files for specific features and scenarios.

---

## Continuous Integration
The project includes CI/CD workflows defined in:
- **`.github/workflows/build.yml`**: Workflow for running tests and other automated tasks on GitHub Actions.
- **`azure-pipelines-2.yml`**: Azure Pipelines configuration for CI/CD integration.

---

## Contribution Guidelines
1. Follow PEP 8 standards for Python code.
2. Write descriptive test names and add comments where necessary.
3. Before raising a pull request, ensure all tests pass locally by running:
   ```bash
   pytest
   ```
4. Update the `requirements.txt` file if new dependencies are added.


## Contribution
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

Happy Testing!
