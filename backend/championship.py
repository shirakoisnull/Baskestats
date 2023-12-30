from flask import Flask, request,  jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import pymysql
import os

#Install requirements with pip install --upgrade -r requirements.txt

app = Flask(__name__)
CORS(app)

load_dotenv()

db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name=os.environ['DB_NAME']

db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

def sqlInj(*values):
    forbidden_symbols = ['@', '!']
    for value in values:
        if any(symbol in str(value) for symbol in forbidden_symbols):
            return True
    return False


# Get list of all championship
@app.route('/championships', methods=['GET'])
def getChamps():
    try:

        cursor = db.cursor()

        cursor.execute('SELECT * FROM championship')
        results=cursor.fetchall()

        return jsonify(results)

    except Exception as e:
        return jsonify({'error': f'Error get championships: {str(e)}'}), 500

    finally:
        cursor.close()

# Create new championship
@app.route('/championships', methods=['POST'])
def createChamp():
    try:
        # Requesting variables
        cYear = request.json.get('cYear')
        if sqlInj(cYear):
            return jsonify({'error': 'Invalid input detected. SQL injection attempt detected.'}), 400

        cursor = db.cursor()
        function = 'CreateChampionship(%s)'
        cursor.execute(f"SELECT {function}", (cYear))
        db.commit()

        # Updates page with all championships
        return 'Success'

    except Exception as e:
        return jsonify({'error': f'Error creating championship: {str(e)}'}), 500

    finally:
        cursor.close()

# Update selected championship
@app.route('/championships/<int:cId>', methods=['PUT'])
def updateChampionship():
    try:
        # Requesting variables
        cYear = request.json.get('cYear')
        cId = request.json.get('cId')
        if sqlInj(cYear):
            return jsonify({'error': 'Invalid input detected. SQL injection attempt detected.'}), 400

        cursor = db.cursor()
        function = 'UpdateChampionship(%s, %s)'
        cursor.execute(f"SELECT {function}", (cId,cYear))
        db.commit()

        return 'Success'

    except Exception as e:
        return jsonify({'error': f'Error updating championship: {str(e)}'}), 500

    finally:
        cursor.close()

# View championship's page
@app.route('/championships/<int:cId>', methods=['GET'])
def viewChampionsip():
    try:
        # Requesting variables
        cId = request.json.get('cId')
        if sqlInj(cId):
            return jsonify({'error': 'Invalid input detected. SQL injection attempt detected.'}), 400

        cursor = db.cursor()
        cursor.execute('SELECT * FROM championship WHERE CID = %s', (cId))
        result=cursor.fetchone()

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': f'Error viewing championship: {str(e)}'}), 500

    finally:
        cursor.close()


@app.route('/championships/<int:cId>', methods=['DELETE'])
def deleteChampionship():
    try:
            cId = request.json.get('cId')
            if sqlInj(cId):
                return jsonify({'error': 'Invalid input detected. SQL injection attempt detected.'}), 400

            with db.cursor() as cursor:

                #Edw mporei aplws na alajei to db na mpei CID ON DELETE CASCADE
                # Delete match results
                cursor.execute('DELETE FROM matchresult WHERE MID IN (SELECT MID FROM matches WHERE CID = %s)', (cId,))

                # Delete matches
                cursor.execute('DELETE FROM match WHERE CID = %s', (cId,))

                # Delete championship
                cursor.execute('DELETE FROM championship WHERE CID = %s', (cId,))

                db.commit()

            return jsonify({'message': 'Success'}), 200
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500
    finally:
        db.close()


if __name__ == '__main__':
    app.run(port=5004)
