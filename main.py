from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/venues')
def venues():
    return render_template('venues.html')

@app.route('/catering')
def catering():
    return render_template('catering.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/destination')
def destination():
    return render_template('destination.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)  # Default: host='127.0.0.1', port=5000
