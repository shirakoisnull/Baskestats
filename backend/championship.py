from flask import Flask, request,  jsonify 
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


# Get list of all championship or just the searched one
@app.route('/championships', methods=['GET'])
def getChamps():
  
    cursor = db.cursor()
 
    cursor.execute('SELECT * FROM championship')
    results=cursor.fetchall()
    cursor.close
    return jsonify(results)

# Create new championship
@app.route('/championships', methods=['POST'])
def createChamp():
    # Requesting variables
    cYear = request.json.get('cYear')
    symbols_present = any('@' in var or '!' in var for var in [  str(cYear) ])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    function = 'CreateChampionship(%s)'
    cursor.execute(f"SELECT {function}", (cYear))
    db.commit()
    cursor.close()
    # Updates page with all championships
    return 'Success'

# Update selected championship
@app.route('/championships/<int:cId>', methods=['PUT'])
def updateChampionship():
     # Requesting variables
    cYear = request.json.get('cYear')
    symbols_present = any('@' in var or '!' in var for var in [  str(cYear) ])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    function = 'UpdateChampionship(%s, %s, %s, %s, %s)'
    cursor.execute(f"SELECT {function}", (cYear))
    db.commit()
    cursor.close()
    return 'Success'

# View championship's page
@app.route('/championships/<int:cId>', methods=['GET'])
def viewChampionsip():
    # Requesting variables
    cId = request.json.get('cId')
    symbols_present = any('@' in var or '!' in var for var in [  str(cId) ])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    cursor.execute('SELECT * FROM championship WHERE CID = %s', (cId))
    result=cursor.fetchone()
    cursor.close()
    return jsonify(result)

# Delete selected championship
@app.route('/championships/<int:cId>', methods=['DELETE'])
def deleteChampionship():
    # Requesting variables
    cId = request.json.get('cId')
    symbols_present = any('@' in var or '!' in var for var in [  str(cId) ])
    if symbols_present:
        return 'Error'
    cursor = db.cursor()
    function = 'DeleteChampionship(%s)'
    cursor.execute(f"SELECT {function}", (cId))
    db.commit()
    cursor.close()
    return 'Success'
       
if __name__ == '__main__':
    app.run(port=5004)


    
