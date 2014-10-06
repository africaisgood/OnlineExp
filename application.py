#!/usr/bin/env python

from flask import request
from flask import Flask, session, jsonify
from flask import render_template, redirect

import json
from uuid import uuid4 as uuid
from datetime import datetime as dt

from babyface import BabyFaceExp
from models import db, User_cond, Response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/cly/Documents/py_practice_code/database/database.db'
db.init_app(app)
# db.create_all()

@app.route('/home/')
def runBabyFace():
	if 'uuid' not in session:
		session['uuid'] = str(uuid())
		experiment = BabyFaceExp(userid=session['uuid'])
		trials = experiment.get('cond')
		user_condition = User_cond(uuid=session['uuid'], trials=trials)
		db.session.add(user_condition)
		db.session.commit()

	else:
		experiment = BabyFaceExp(userid=session['uuid'])
		trials = experiment.get('cond')	

	session['trialNum'] = session.get('trialNum', 0)
	if session['trialNum'] == 8:
		return redirect('/thanks/')
	return render_template('babyFaceExp.html', img_name=trials[session['trialNum']])

@app.route('/API/answer/', methods=['GET', 'POST'])
def answer():
	data = request.form.get('answer', '')
	if data == '':
		return jsonify(status='failed', error='no result')
	else:
		if session['trialNum'] < 8:
			timestamp = dt.now()
			user_response = Response(uuid=session['uuid'], trial_num=session['trialNum'], answer=data, timestamp=timestamp)
			db.session.add(user_response)
			db.session.commit()					
			session['trialNum'] += 1 
		return jsonify(status='success',error='')

GENDER = {'male': 'M', 'female': 'F'}
@app.route('/thanks/')
def check_ans():
	hits = 0
	misses = 0
	curr_subj = User_cond.query.filter_by(uuid=session['uuid']).first()
	subj_ans = Response.query.filter_by(uuid=session['uuid']).all()

	for i in xrange(8):
		right_ans = curr_subj.trials.split(',')[i]
		subj_ans[i].answer = GENDER[subj_ans[i].answer]
		if subj_ans[i].answer == 'M':
			if subj_ans[i].answer in right_ans:
				print 'Hit!'
				hits += 1
			else:
				print 'Miss!'
				misses += 1			
		elif subj_ans[i].answer == 'F':
			# hits += 1 if subj_ans[i].answer in right_ans 
			# misses += 1 if subj_ans[i].answer not in right_ans
			if subj_ans[i].answer in right_ans:
				print 'Hit!'
				hits += 1
			else:
				print 'Miss!'
				misses += 1	
	all_items = hits + misses
	return render_template('thanks.html', hits=hits, all_items=all_items)

@app.route('/clear/')
def clear():
	session.clear()
	return redirect('/home/')

if __name__ == '__main__':
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmxcvbxcbghert'
	app.run(debug=True)

