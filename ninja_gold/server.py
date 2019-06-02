
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'helloworld'

@app.route('/')
def index():
    if 'score' not in session:
        session['score'] = 0    
   
    return render_template("index.html")
@app.route('/process_money', methods=["POST"])
def process_money():
    if request.form['building'] == 'farm':
        session['score'] += random.randint(10,20)
        return redirect("/")
    if request.form['building'] == 'house':
        session['score'] += random.randint(5,10)
        return redirect("/")
    if request.form['building'] == 'cave':
        session['score'] += random.randint(2,5)
        return redirect("/")
    if request.form['building'] == 'casino':
        session['score'] += random.randint(-50,50) 
        return redirect("/")
    return redirect("/")
@app.route("/reset", methods=['POST'])
def reset():
    session['score'] = 0
    session.clear()
    return redirect('/')
app.run(debug=True)