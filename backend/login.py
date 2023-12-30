from flask import Flask, request, url_for, redirect, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import pymysql
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


#Install requirements with pip install --upgrade -r requirements.txt

app = Flask(__name__)
CORS(app)

load_dotenv()

db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name=os.environ['DB_NAME']

app.config["JWT_SECRET_KEY"] = os.environ['JWT_SECRET_KEY']
jwt = JWTManager(app)

db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

def sqlInj(*values):
    forbidden_symbols = ['@', '!']
    for value in values:
        if any(symbol in str(value) for symbol in forbidden_symbols):
            return True
    return False



# Logging in
@app.route('/login',methods=['POST'])
def login():
        # Gets the username and password from the input form of the frontend
        username = request.json.get('username')
        password = request.json.get('password')

        if sqlInj(username,password ):
            return jsonify({'error': 'Invalid input detected. SQL injection attempt detected.'}), 400


        # Making a cursor/pointer object for interacting with the database
        cursor = db.cursor()
        # Executing the query using parametirised variables using the %s placeholder for preventing SQL injections
        cursor.execute('SELECT password FROM secretary WHERE username = %s',(username,))
        # Fetching one instance
        result=cursor.fetchone()
        cursor.close()

        # Checking if result exists and is equal to my password
        if result and result[0] == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token, username)
        else:
            return 'Error'

#Gettng current user
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
     current = get_jwt_identity()
     return jsonify(user=current), 200



if __name__ == '__main__':
    app.run(port=5001)
