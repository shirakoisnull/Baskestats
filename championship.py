from flask import Flask, request, url_for, redirect, jsonify, render_template
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
    search = request.json.get['search']
    cursor = db.cursor()
    if search is None or search.strip() == '':
        cursor.execute('SELECT * FROM championship')
    else:
        cursor.execute('SELECT * FROM championship WHERE year LIKE %s', ('%' + search + '%',))
    results=cursor.fetchall()
    cursor.close
    return jsonify(results)

# Create new championship
@app.route('/championship', methods=['POST'])
def createChamp(champ_year):

    cursor = db.cursor()
    function = 'CreateChampionship(%s)'
    cursor.execute(f"SELECT {function}", (champ_year))
    db.commit()
    cursor.close()
    # Updates page with all championships
    return redirect(url_for('getChamps'))

# Update selected championship
@app.route('/championships/<int:cId>', methods=['PUT'])
def updateChampionship(champ_year):
    cursor = db.cursor()
    function = 'UpdateChampionship(%s, %s, %s, %s, %s)'
    cursor.execute(f"SELECT {function}", (champ_year))
    db.commit()
    cursor.close()
    return redirect(url_for('getChamps'))

# View championship's page
@app.route('/championships/<int:cId>', methods=['GET'])
def viewChampionsip(cId):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM championship WHERE CID LIKE %s', (cId))
    result=cursor.fetchone()
    cursor.close()
    return jsonify(result)

# Delete selected championship
@app.route('/championships/<int:cId>', methods=['DELETE'])
def deletePlayer(cId):
    cursor = db.connection.cursor()
    function = 'DeleteChampionship(%s)'
    cursor.execute(f"SELECT {function}", (cId))
    db.commit()
    cursor.close()
    return jsonify("Success!")
       
if __name__ == '__main__':
    app.run(port=5004)


    