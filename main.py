from flask import Flask, Response, redirect, url_for, request, session, abort
from flask import escape
from flask import render_template
import time
import simplejson as json
from SignUpSave import *
from PasswordEnocde import *
from Login import *
from RentRequestSave import *
from Filter_Nest import *
from HouseForRentSave import *


from flask_login import LoginManager, UserMixin, \
								login_required, login_user, logout_user, current_user


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
	pass

# all users in database
'''
users = [
	{'id': 'Tom', 'email': 'Tom', 'password': '111111'},
	{'id': 'Michael', 'email': 'Michael', 'password': '123456'},
	{'id': 'hello@usc.edu', 'email': 'hello@usc.edu', 'password': '123'}
]
'''
users = []

'''
def query_user(user_id):
	for user in users:
		if user_id == user['id']:
			return user
'''

@login_manager.user_loader
def load_user(user_id):
	print(user_id)
	if queryUser(user_id) :
		curr_user = User()
		curr_user.id = user_id
		return curr_user

@app.route('/test')
def text():
	return render_template('hello.html')

@app.route('/post')
@login_required
def post():
	return 'Post'

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])	
@login_required									 
def index():	
	if request.method == 'POST':
		# filter 
		search = request.form['search']
		roomType = request.form['roomType']
		rt = None if not roomType else int(roomType)
		rentFee = request.form['rentFee']
		rf = None if not rentFee else int(rentFee)
		startDate = request.form['startDate']
		sd = None if not startDate else startDate
		endDate = request.form['endDate']
		ed = None if not endDate else endDate
		distance = request.form['distance']		

		res = Filter(rt, rf, sd, ed, None, None)
		print(res)
		session['filter_res'] = res
		return render_template('texttext.html')
	else:
		#time.sleep( 5 )
		points = []
		if 'filter_res' in session:
			#print(session['filter_res'])
			for item in session['filter_res']:
				points.append({'lat':item['latitude'],'lng':item['longitude'], 'rentFee':item['rentFee'], 'starttime':item['startDate'], 'endtime':item['endDate'], 'description':item['description'], 'imgUrl':item['imgUrl'],'contactInfo':item['contactInfo']});
			session.pop('filter_res',None)
			print(points)
		else:
			res = Filter()
			for item in res:
				points.append({'lat':item['latitude'],'lng':item['longitude'], 'rentFee':item['rentFee'], 'starttime':item['startDate'], 'endtime':item['endDate'], 'description':item['description'], 'imgUrl':item['imgUrl'],'contactInfo':item['contactInfo']});
		return render_template('texttext.html',points=json.dumps(points))
'''																
	points = [{"lat": 43.8934276, "lng": -103.3690243},						 
			  {"lat": 47.052060, "lng": -91.639868},							
			  {"lat": 45.1118, "lng": -95.0396}]								

	return render_template("text.html", points=json.dumps(points)) 
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
	#if current_user.is_authenticated:
	#	return redirect(url_for('index'))

	if request.method == 'POST':
		email = request.form['email']
		password = PasswordEncode(request.form['password'])
		login_result = LogIn(email,password) 
		if login_result[0]:
			user = User()
			user.id = email
			'''
			user.email = temp['email']
			user.name = temp['name']
			user.password = temp['password']
			'''
			login_user(user)
			return redirect(url_for('index'))
		else:
			return redirect(url_for('login'))
	else:
		return render_template('login.html')

'''
def valid_login(email, password, temp):
	print(users)
	print(email)
	print(password)
	for user in users:
		if user['email']==email:
			if user['password'] == password:
				temp = 1*user
				print(temp)
				return True
			else:
				return False
	return False
'''

@app.route('/register', methods=['GET', 'POST'])
def register():
	#if current_user.is_authenticated:
	#	return redirect(url_for('index'))
	#print(request.method)
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']		
		user = User()
		user.name = name
		user.email = email
		user.password = PasswordEncode(password)
		user.id = user.email#
		SignUpSave(user.name,user.email,user.password)

		#users.append({'id':user.id, 'email':email, 'password':user.password, 'name':name})
		login_user(user)
		
		return redirect(url_for('index')) # server side redirect won't work with ajax
		#return render_template('hello.html')
	else:
		#time.sleep( 5 )
		return render_template('signup.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/rentrequest', methods=['GET','POST'])	
@login_required									 
def rentrequest():	
	if request.method == 'POST':	
		contactInfo = request.form['contactInfo']
		rentFee = request.form['rentFee']
		startTime = request.form['startTime']
		endTime = request.form['endTime']
		requirement = request.form['requirement']
		RentRequestSave({'rent_fee':rentFee, 'starttime':startTime, 'endtime':endTime, 'contact_info':contactInfo, 'requirement':requirement});
		return render_template('texttext.html')
	else:
		
		return render_template('rentRequest.html')

@app.route('/rentpost', methods=['GET','POST'])	
@login_required									 
def rentpost():	
	if request.method == 'POST':	
		contactInfo = request.form['contactInfo']
		rentFee = request.form['rentFee']
		startTime = request.form['startTime']
		endTime = request.form['endTime']
		address = request.form['address']
		description = request.form['description']
		lat = request.form['lat']
		lng = request.form['lng']
		housetype = '1'
		imgUrl = "https://images.unsplash.com/photo-1501183638710-841dd1904471?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80"
		HouseForRentSave({'latitude':lat,'longitude':lng, 'type':housetype, 'rent_fee':rentFee, 'starttime':startTime, 'endtime':endTime, 'contact_info':contactInfo, 'description':description,'image':imgUrl});
		return render_template('texttext.html')
	else:
		
		return render_template('houseInfo.html')