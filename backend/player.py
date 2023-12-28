from flask import Flask,  jsonify, request
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

# Get list of all players or just the searched one
@app.route('/players', methods=['GET'])
def getPlayers():
    cursor = db.cursor()
    cursor.execute('''
                    SELECT player.*, team.name
                    FROM player
                    LEFT JOIN team ON player.TID = team.TID
                    WHERE player.TID IS NOT NULL OR team.TID IS NULL;
                   ''')
    results=cursor.fetchall()
   
    cursor.close
    return jsonify(results)
    
# Create new player
@app.route('/players', methods=['POST'])
def createPlayer():
    # Requesting variables
    pName = request.json.get['pName'] 
    pAge = request.json.get['pAge']
    pHeight = request.json.get['pHeight']
    pWeight = request.json.get['pWeight']
    pPoints = request.json.get['pPoints']
    
    #Checking for @ and ! symbols for SQL injection
    symbols_present = any('@' in var or '!' in var for var in [pName, str(pAge), str(pHeight), str(pWeight), str(pPoints)])
    if symbols_present:
        return 'Error'
    

    cursor = db.cursor()
    function = 'CreatePlayer(%s, %s, %s, %s, %s)'
    cursor.execute(f"SELECT {function}", (pName, pAge, pHeight, pWeight, pPoints))
    db.commit()

    cursor.close()

    return 'Success'

# Associate player with team
@app.route('/associate', methods=['POST'])
def associatePlayerTeam():
    # Requesting variables
    pId = request.json.get['pId']
    teamId = request.json.get['teamId']
    #Checking for @ and ! symbols for SQL injection
    symbols_present = any('@' in var or '!' in var for var in [ str(pId), str(teamId)])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    function = 'AssociatePlayerTeam(%s, %s)'
    cursor.execute(f"SELECT {function}", (pId, teamId))
    db.commit()
    cursor.close()
    return 'Success'

# Update selected player
@app.route('/players/<int:pId>', methods=['PUT'])
def updatePlayer():

    # Requesting variables
    pName = request.json.get['pName'] 
    pAge = request.json.get['pAge']
    pHeight = request.json.get['pHeight']
    pWeight = request.json.get['pWeight']
    pPoints = request.json.get['pPoints']
    pId = request.json.get['pId']
    # Checking for @ and ! symbols for SQL injection
    symbols_present = any('@' in var or '!' in var for var in [pName,str(pId), str(pAge), str(pHeight), str(pWeight), str(pPoints)])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    function = 'UpdatePlayer(%s, %s, %s, %s, %s)'
    cursor.execute(f"CALL {function}", (pId, pName, pAge, pHeight, pWeight, pPoints))
    db.commit()
    cursor.close()
    return 'Success'

# View player's page
@app.route('/players/<int:pId>', methods=['GET'])
def viewPlayer():
    pId = request.json.get['pId']
    symbols_present = any('@' in var or '!' in var for var in [str(pId)])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    cursor.execute('SELECT * FROM players WHERE PID = %s', (pId))
    result=cursor.fetchone()
    cursor.close()
    return jsonify(result)

# Delete selected player
@app.route('/players/<int:pId>', methods=['DELETE'])
def deletePlayer():
    pId = request.json.get['pId']
    symbols_present = any('@' in var or '!' in var for var in [str(pId)])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    function = 'DeletePlayer(%s)'
    cursor.execute(f"SELECT {function}", ({pId}))
    db.commit()
    cursor.close()
    return 'Success'
       
 
 
        
if __name__ == '__main__':
    app.run(port=5002)


    