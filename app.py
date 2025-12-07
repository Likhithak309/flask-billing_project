from flask import Flask, render_template, request
import sqlite3
import json

app = Flask(__name__)

# ------------------------
# Initialize database
# ------------------------
def init_db():
    conn = sqlite3.connect('bills.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            items TEXT,
            total REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ------------------------
# Home page
# ------------------------
@app.route('/')
def home():
    return render_template('index.html')

# ------------------------
# Calculate bill route
# ------------------------
@app.route('/calculate', methods=['POST'])
def calculate_bill():
    items = request.form.getlist('item')
    quantities = request.form.getlist('quantity')
    prices = request.form.getlist('price')
    tax = request.form.get('tax', 0)
    discount = request.form.get('discount', 0)

    bill_items = []
    subtotal = 0

    # Safely convert tax and discount
    try:
        tax = float(tax)
        discount = float(discount)
    except:
        tax = 0
        discount = 0

    # Process each item
    for i in range(len(items)):
        try:
            qty = float(quantities[i])
            price = float(prices[i])
            total = qty * price
            bill_items.append({'item': items[i], 'quantity': qty, 'price': price, 'total': total})
            subtotal += total
        except:
            return "Invalid input for quantity or price.<br><a href='/'>Go Back</a>"

    # Calculate grand total
    grand_total = subtotal + (subtotal * tax / 100) - discount

    # Save bill to DB as JSON
    conn = sqlite3.connect('bills.db')
    c = conn.cursor()
    c.execute("INSERT INTO bills (items, total) VALUES (?, ?)", (json.dumps(bill_items), grand_total))
    conn.commit()
    conn.close()

    # Render bill template with all values
    return render_template('bill.html', bill_items=bill_items, subtotal=subtotal,
                           tax=tax, discount=discount, grand_total=grand_total)

# ------------------------
# Run the app
# ------------------------

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
