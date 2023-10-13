from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('Home.html')

@app.route('/market')
def market_page():
    items =[{"id":1,"Name":"phone","Barcode":"893212299897","price":500},
    {"id":2,"Name":"Laptop","Barcode":"123985473165","price":900},
    {"id":3,"Name":"Keyboard","Barcode":"231985128446","price":150}]

    return render_template('market.html',items=items)

if __name__ == '__main__':
    app.run(debug=1)
