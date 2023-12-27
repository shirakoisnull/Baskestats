from flask import Flask,  jsonify
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
def createPlayer(pName, pAge, pHeight, pWeight, pPoints):
    cursor = db.cursor()
    function = 'CreatePlayer(%s, %s, %s, %s, %s)'
    cursor.execute(f"SELECT {function}", (pName, pAge, pHeight, pWeight, pPoints))
    db.commit()

    cursor.close()

    return 'Success'

# Associate player with team
@app.route('/players', methods=['POST'])
def associatePlayerTeam(pId, teamId):
    cursor = db.cursor()
    function = 'AssociatePlayerTeam(%s, %s)'
    cursor.execute(f"SELECT {function}", (pId, teamId))
    db.commit()
    cursor.close()
    return 'Success'

# Update selected player
@app.route('/players/<int:pId>', methods=['PUT'])
def updatePlayer(pId, pName, pAge, pHeight, pWeight, pPoints):
    cursor = db.cursor()
    function = 'UpdatePlayer(%s, %s, %s, %s, %s)'
    cursor.execute(f"CALL {function}", (pId, pName, pAge, pHeight, pWeight, pPoints))
    db.commit()
    cursor.close()
    return 'Success'

# View player's page
@app.route('/players/<int:pId>', methods=['GET'])
def viewPlayer(pId):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM players WHERE PID = %s', (pId))
    result=cursor.fetchone()
    cursor.close()
    return jsonify(result)

# Delete selected player
@app.route('/players/<int:pId>', methods=['DELETE'])
def deletePlayer(pId):
    cursor = db.cursor()
    function = 'DeletePlayer(%s)'
    cursor.execute(f"SELECT {function}", ({pId}))
    db.commit()
    cursor.close()
    return 'Success'
       
 
 
        
if __name__ == '__main__':
    app.run(port=5002)


    