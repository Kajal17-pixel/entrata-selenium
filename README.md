# Entrata Selenium Automation (Python + Pytest)

This is a Selenium automation framework to test [Entrata.com](https://www.entrata.com) using Python with the Pytest framework.

## ✅ Features
- Python + Selenium
- Page Object Model (POM)
- Pytest with setup/teardown fixtures
- Screenshots on failure
- HTML reports (via `pytest-html`)
- Logging using Loguru

## 🛠 Setup Instructions

### 1. Clone the repo / download project

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run tests
```bash
python -m pytest --html=reports/html_report.html --self-contained-html
```

### 4. View logs & reports
- **Logs:** `reports/logs/test_log.log`
- **Screenshots (on failure):** `reports/screenshots/`
- **HTML Report:** `reports/html_report.html`

## 🧪 Test Cases
1. Check if title contains "Entrata"
2. Navigate to **ProspectPortal** via hover
3. Navigate to **Careers** at page bottom

## ❗ Notes
- Not submitted any form (only view/navigation tests)
- Explicit waits used throughout (no sleep())