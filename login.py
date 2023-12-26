from flask import Flask, request, session, url_for, redirect, render_template, jsonify
from dotenv import load_dotenv
import pymysql
import os
from flask_jwt_extended import JWTManager


#Install requirements with pip install --upgrade -r requirements.txt 

app = Flask(__name__)

load_dotenv()

db_host = os.environ['DB_HOST'] 
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name=os.environ['DB_NAME']

app.config["JWT_SECRET_KEY"] = os.environ['JWT_SECRET_KEY']
jwt = JWTManager(app)



 


db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
  

# Checks if user is logged in or not
def secretary():
    if 'username' in session:
       return jsonify(logged_in=True, username=session['username'])
    else:
        # User is not logged in
        return jsonify(logged_in=False)

# Reloads page and passes secretary value thats either True or False
@app.route('/')
def index():
    return render_template('index.html', secretary=secretary())

# Logging in
@app.route('/login',methods=['POST'])
def login():
        # Gets the username and password from the input form of the frontend
        username = request.json.get['username'] 
        password = request.json.get['password']
        
        # Making a cursor/pointer object for interacting with the database
        cursor = db.connection.cursor()
        # Executing the query using parametirised variables using the %s placeholder for preventing SQL injections
        cursor.execute('SELECT password FROM secretary WHERE username = %s',(username,))
        # Fetching one instance
        result=cursor.fetchone()
        cursor.close
        # Checking if result exists and is equal to my password
        if result and result[0] == password:
            # Adds user to session
            session['username']=username
            #access_token = create_access_token(identity=username)
            #return jsonify(access_token, username)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('error'))

# Logging out
@app.route('/logout')
def logout():

    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()


# Kai meta sto index elegxei ean einai admin me {% if secretary %} {% endif %}
    