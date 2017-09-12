from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 's@54e236ecr8v0x8972f@#$5vs!$'

@app.route("/")
def index():
	if not'gold_amount' in session:
		session['gold_amount'] = 0

	if not 'activitylist' in session:
		session['activitylist'] = []

	return	render_template('index.html', gold = session['gold_amount'])

@app.route("/process_money", methods=["post"])
def process():
	getgold = request.form['building']

	if getgold == 'farm':
		earnedgold = random.randint(10,21)
		session['gold_amount'] += earnedgold
		session['message'] = "Earned "+str(earnedgold)+" gold from the farm!"
		session['activitylist'].insert(0,session['message'])

	elif getgold == 'cave':
		earnedgold = random.randint(5,11)
		session['gold_amount'] += earnedgold
		session['message'] = "Earned "+str(earnedgold)+" gold from the cave!"
		session['activitylist'].insert(0,session['message'])

	elif getgold == 'house':
		earnedgold = random.randint(2,6)
		session['gold_amount'] += earnedgold
		session['message'] = "Earned "+str(earnedgold)+" gold from the house!"
		session['activitylist'].insert(0,session['message'])

	elif getgold == 'casino':
		earnedgold = random.randint(0,51)
		session['gold_amount'] += earnedgold
		session['message'] = "Earned "+str(earnedgold)+" gold from the casino!"
		session['activitylist'].insert(0,session['message'])

	return	redirect("/")

app.run(debug=True)