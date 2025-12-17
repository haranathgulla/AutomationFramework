# Automation Framework (Selenium + PyTest)

This repository contains a **Python-based Test Automation Framework** built using **Selenium WebDriver**, **PyTest**, and **Page Object Model (POM)**. The framework is designed for UI automation with clean structure, reusability, and reporting support.

---

## 📌 Project Overview

* Language: **Python 3.13**
* Automation Tool: **Selenium WebDriver**
* Test Framework: **PyTest**
* Design Pattern: **Page Object Model (POM)**
* Reporting: **pytest-html**
* IDE: **PyCharm**
* Version Control: **Git & GitHub**

---

## 📁 Project Structure

```
AutomationFramework
│
├── tests/                 # Test cases
│   └── test_login.py
│
├── pages/                 # Page Object classes
│   └── login_page.py
│
├── utils/                 # Browser & utility setup
│   └── base_driver.py
│
├── reports/               # HTML reports (ignored in git)
│
├── pytest.ini             # PyTest configuration
├── requirements.txt       # Project dependencies
├── .gitignore             # Files ignored by Git
└── README.md              # Project documentation
```

---

## ⚙️ Prerequisites

Make sure the following are installed:

* Python **3.9+** (Recommended: 3.13)
* Google Chrome browser
* PyCharm (Community / Professional)
* Git

---

## 📦 Install Dependencies

Create virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run Tests

Run all test cases:

```bash
pytest -v
```

---

## 📊 Generate HTML Report

Run tests with HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Open the report:

* Navigate to `reports/report.html`
* Open it in any browser

---

## ✅ Sample Test Covered

* Valid Login Test

  * Application: [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)
  * Validates successful login using success message

---

## 🧠 Key Features

✔ Page Object Model (POM)
✔ Explicit waits for stability
✔ Reusable browser setup
✔ Clean folder structure
✔ HTML reporting
✔ GitHub version control

---

## 🚀 Future Enhancements

* Screenshot capture on failure
* Logging support
* Data-driven testing (Excel / CSV)
* Allure reporting
* GitHub Actions (CI/CD)

---

## 👤 Author

**Haranath Gulla**
QA Automation Engineer

---

## 📄 License

This project is for learning and demonstration purposes.
