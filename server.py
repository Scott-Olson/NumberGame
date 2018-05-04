from flask import Flask, render_template, request, redirect, session
import math, random

app=Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def drawBase():
	temp = random.randrange(0,101)
	if 'answer' not in session:
		session['answer'] = temp
	return render_template('index.html', answer = session['answer'])

@app.route('/guess', methods=['POST'])
def drawGuess():
	temp1 = int(request.form['guess'])
	if temp1 == int(session['answer']):
		compVal = 'winner'
		compText = 'Good job! Play again?'
	if temp1 > int(session['answer']):
		compVal = 'higher'
		compText = 'Too high, guess again'
	if temp1 < int(session['answer']):
		compVal = 'lower'
		compText = 'Too low, guess again'
	print(request.form)
	return render_template('index.html', retVal = compVal, retText = compText)

@app.route('/reset')
def resetButton():
	session.clear()
	return redirect('/')


app.run(debug=True)