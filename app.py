from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Billing route
@app.route('/calculate', methods=['POST'])
def calculate():
    items = request.form.getlist('item')
    quantities = request.form.getlist('quantity')
    prices = request.form.getlist('price')

    bill_items = []
    grand_total = 0

    for i in range(len(items)):
        try:
            qty = float(quantities[i])
            price = float(prices[i])
            total = qty * price
            bill_items.append({
                'item': items[i],
                'quantity': qty,
                'price': price,
                'total': total
            })
            grand_total += total
        except:
            return "Invalid input. Please enter numbers for quantity and price.<br><a href='/'>Go Back</a>"

    return render_template('bill.html', bill_items=bill_items, grand_total=grand_total)

# ---------- IMPORTANT FOR RENDER ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
