from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('question.html')

@app.route('', methods=[''])
def result():
    q1 = request.form['']
    q2 = request.form['']
    q3 = request.form['']
    advice = request.form['']

    return render_template('result.html')

app.run(port=5002, debug=True)
