# 💸 MoneyPulse - Expense Tracker Dashboard

MoneyPulse is a Flask-based web application that helps users track their expenses with visual insights. Users can enter their daily or weekly expenses and view them through interactive charts like:

- 📊 Category-wise expense chart
- 📈 Monthly trend analysis
- 📉 Budget vs Actual spending

## 🔧 Features

- Add, view, and manage expenses
- Visualizations using matplotlib
- Dashboard to track and analyze spending
- Organized project structure for scalability

## 🗂️ Project Structure
expense/
├── static/
│ └── charts/ # Generated chart images
├── templates/
│ ├── main.html # Base template
│ ├── home.html # Home page
│ └── dashboard.html # Expense dashboard with charts
├── init.py # Flask app initialization
├── models.py # Database models
├── routes.py # Routes and logic
instance/
└── run.py # App entry point



## 🚀 How to Run

1. **Clone the repo:**

```bash
git clone https://github.com/pankajkumar8709/Expense-Tracker.git
cd Expense-Tracker

