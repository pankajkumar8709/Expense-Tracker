from expense import app,db
from flask import render_template,redirect,request
from expense.models import expenses
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from collections import defaultdict

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/main',methods=['POST','GET'])
def main():
    return render_template('main.html')
@app.route('/add',methods=['POST'])
def add():
    if request.method=='POST':
        amount=request.form['amount']
        category=request.form['category']
        date_str=request.form['date']
        description=request.form['description']

        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        exp=expenses(amount=amount,category=category,date=date,description=description)
        db.session.add(exp)
        db.session.commit()
        return redirect('dashboard')
    

@app.route('/dashboard')
def dashboard():
    all_expenses = expenses.query.all()

    # Total expenses
    total_expenses = sum(float(e.amount) for e in all_expenses)

    # Group by category
    category_data = defaultdict(float)
    for e in all_expenses:
        category_data[e.category] += float(e.amount)

    # Group by month
    monthly_data = defaultdict(float)
    for e in all_expenses:
        # date_obj = datetime.strptime(e.date, '%Y-%m-%d')
        month = e.date.strftime('%b %Y')
        monthly_data[month] += float(e.amount)

    # Dummy budget data (adjust as needed)
    budget = 20000  # or pull from DB/user input
    actual = total_expenses

    # Save all charts
    chart_path = os.path.join(app.root_path, 'static', 'charts')
    os.makedirs(chart_path, exist_ok=True)

    # Category-wise chart
    plt.figure(figsize=(6, 4))
    plt.bar(category_data.keys(), category_data.values(), color='skyblue')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount (₹)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(chart_path, 'category_chart.png'))
    plt.close()

    # Monthly trend chart
    sorted_months = sorted(monthly_data.items(), key=lambda x: datetime.strptime(x[0], '%b %Y'))
    months, monthly_amounts = zip(*sorted_months)

    plt.figure(figsize=(6, 4))
    plt.plot(months, monthly_amounts, marker='o', linestyle='-', color='green')
    plt.title('Monthly Expense Trend')
    plt.xlabel('Month')
    plt.ylabel('Amount (₹)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(chart_path, 'monthly_trend.png'))
    plt.close()

    # Budget vs Actual Pie Chart
    plt.figure(figsize=(5, 5))
    plt.pie([actual, max(0, budget - actual)], labels=['Spent', 'Remaining'],
            colors=['red', 'lightgreen'], autopct='%1.1f%%')
    plt.title('Budget vs Actual')
    plt.savefig(os.path.join(chart_path, 'budget_vs_actual.png'))
    plt.close()

    return render_template('dashboard.html', all_expenses=all_expenses,total_expenses=total_expenses,
                           timestamp=datetime.now().timestamp())