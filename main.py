from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hola, welcome to my Flask learning"

@app.route("/index", methods = ['GET'])
def index():
    return jsonify({"message": "Hello, this is the index route."})
    #render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Helo {name}!!'

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "Pass"
    else:
        res = "Fail misserably"

    expression = {'score': score, 'res':res}    

    return render_template("result1.html",  results = expression)


if __name__ == "__main__":
    app.run(debug=True)