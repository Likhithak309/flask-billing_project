from flask import Flask, render_template, request  # import what you use

app = Flask(__name__)

# Example route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bill', methods=['POST'])
def generate_bill():
    # Your billing logic here
    return render_template('bill.html')

# This is important for local testing
if __name__ == "__main__":
    app.run(debug=True)
