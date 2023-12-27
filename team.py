from flask import Flask, jsonify 
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
def createTeam(team_name, team_city, team_wins, team_losses):

    cursor = db.cursor()
    function = 'CreateTeam(%s, %s, %s, %s, %s)'
    cursor.execute(f"SELECT {function}", (team_name, team_city, team_wins, team_losses))
    db.commit()
    cursor.close()
    # Updates page with all teams
    return 'Success'

# Update selected team
@app.route('/teams/<int:tId>', methods=['PUT'])
def updateTeam(tId, team_name, team_city, team_wins, team_losses):
    cursor = db.cursor()
    function = 'UpdateTeam(%s, %s, %s, %s, %s)'
    cursor.execute(f"SELECT {function}", (tId, team_name, team_city, team_wins, team_losses))
    db.commit()
    cursor.close()
    return  'Success'

# View team's page
@app.route('/teams/<int:tId>', methods=['GET'])
def viewTeam(tId):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM teams WHERE TID = %s', (tId))
    result=cursor.fetchone()
    cursor.close()
    return jsonify(result)

# Delete selected team
@app.route('/teams/<int:tId>', methods=['DELETE'])
def deleteTeam(tId):
    cursor = db.cursor()
    function = 'DeleteTeam(%s)'
    cursor.execute(f"SELECT {function}", (tId))
    db.commit()
    cursor.close()
    return 'Success'
       
if __name__ == '__main__':
    app.run(port=5003)


    