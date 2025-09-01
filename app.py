from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
	with open('home.html','r') as file:
		return file.read()

@app.route('/id/<user_id>')
def get_user_data(user_id):
	with open('users.json', 'r')as file:
		users = json.load(file)
		try:
			user = users[f"{user_id}"]
			user_data = {
			"name":user,
			"id":user_id,
			"email":"QHasGone@example.com",
			"password":"AEZAKMI"
			}
			extra = request.args.get("extra")
			if extra:
				user_data["extra"] = extra
				return jsonify(user_data), 200
		except:
			return "User not found!"
		

@app.route('/signup', methods=["POST"])
def register():
	data = request.get_json()
	print(data)
	return jsonify(data), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080,debug=True)
	

def get_image():
	url = 'https://dog.ceo/api/breeds/image/random'
	
# http://127.0.0.1:5000/id/20999?extra=abcd
