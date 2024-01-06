from flask import Flask, jsonify , request
from dotenv import load_dotenv
import pymysql
import os

#Install requirements with pip install --upgrade -r requirements.txt 

app = Flask(__name__)

load_dotenv()

db_host = os.environ['DB_HOST'] 
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name=os.environ['DB_NAME']

db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)


# Get list of all teams or just the searched one
@app.route('/teams', methods=['GET'])
def getTeams():
  
    cursor = db.cursor()
    cursor.execute('SELECT * FROM team')
    results=cursor.fetchall()
    cursor.close
    return jsonify(results)

# Create new team
@app.route('/teams', methods=['POST'])
def createTeam():
    # Requesting variables
    tName = request.json.get('tName')
    tCity = request.json.get('tCity')
    tWins = request.json.get('tWins')
    tLosses = request.json.get('tLosses')
 
    #Checking for @ and ! symbols for SQL injection
    symbols_present = any('@' in var or '!' in var for var in [tName, tCity, str(tWins), str(tLosses)])
    if symbols_present:
        return 'Error'
    
    cursor = db.cursor()
    function = 'CreateTeam(%s, %s, %s, %s)'
    cursor.execute(f"SELECT {function}", (tName, tCity, tWins, tLosses))
    db.commit()
    cursor.close()
   
    return 'Success'

# Update selected team
@app.route('/teams/<int:tId>', methods=['PUT'])
def updateTeam( ):
    # Requesting variables
    tName = request.json.get('tName')
    tCity = request.json.get('tCity')
    tWins = request.json.get('tWins')
    tLosses = request.json.get('tLosses')
    tId = request.json.get('tId')
 
    #Checking for @ and ! symbols for SQL injection
    symbols_present = any('@' in var or '!' in var for var in [tName, tCity,str(tId), str(tWins), str(tLosses)])
    if symbols_present:
        return 'Error'
    
    cursor = db.cursor()
    function = 'UpdateTeam(%s, %s, %s, %s, %s)'
    cursor.execute(f"SELECT {function}", (tId, tName, tCity, tWins, tLosses))
    db.commit()
    cursor.close()
    return  'Success'

# View team's page
@app.route('/teams/<int:tId>', methods=['GET'])
def viewTeam():
    tId = request.json.get('tId')
 
    #Checking for @ and ! symbols for SQL injection
    symbols_present = any('@' in var or '!' in var for var in [str(tId) ])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    cursor.execute('SELECT * FROM teams WHERE TID = %s', (tId))
    result=cursor.fetchone()
    cursor.close()
    return jsonify(result)

# Delete selected team
@app.route('/teams/<int:tId>', methods=['DELETE'])
def deleteTeam(tId):
    tId = request.json.get('tId')
 
    #Checking for @ and ! symbols for SQL injection
    symbols_present = any('@' in var or '!' in var for var in [str(tId) ])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    function = 'DeleteTeam(%s)'
    cursor.execute(f"SELECT {function}", (tId))
    db.commit()
    cursor.close()
    return 'Success'
       
if __name__ == '__main__':
    app.run(port=5003)


    