# QA Automation: Selenium WebDriver with Page Object Model (Python)

This is a demo automation project using **Selenium WebDriver** and **PyTest**, applying the **Page Object Model (POM)** design pattern.  
The tests are written in **Python** and are designed to be modular, readable, and easily maintainable.

## 📁 Project Structure

```
New_project_sel/
├── page_objects/         # Page classes (POM)
├── tests/                # PyTest test cases
├── requirements.txt      # Python dependencies
├── pytest.ini            # PyTest configuration
└── README.md             # Project documentation
```

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/qa-automation-selenium-pom.git
cd qa-automation-selenium-pom
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run tests with PyTest:
```bash
pytest tests/
```

## ✅ Features

- Selenium WebDriver integration
- PyTest testing framework
- Page Object Model (POM) structure
- Configurable test runner via `pytest.ini`
- Modular and scalable structure

## 📌 Requirements

- Python 3.8+
- pip
- ChromeDriver or GeckoDriver (matching browser version)

## 📄 License

This project is open-source and free to use for learning and personal purposes.

---

Built by [Valentin Popescu]
