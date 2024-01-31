from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])

def login():
	username = request.form['username']
	password = request.form['passward']
	return f"Username: {username} \nPassword: {password}"

if __name__ == "__main__":
	app.run()