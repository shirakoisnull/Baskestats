from flask import Flask, jsonify , request
from dotenv import load_dotenv
from flask_cors import CORS
import pymysql
import math
import os
 

#Install requirements with pip install --upgrade -r requirements.txt 

app = Flask(__name__)
CORS(app)

load_dotenv()


# (╯°□°)╯︵ ┻━┻
# (╯°□°)╯︵ ┻━┻
# (╯°□°)╯︵ ┻━┻
# (╯°□°)╯︵ ┻━┻
# (╯°□°)╯︵ ┻━┻

 


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

 
def matchResult(cId, teams):
    try:
        cursor = db.cursor()
        


        cursor.execute('SELECT MID FROM matches WHERE CID = %s', (cId,))
        mIds = cursor.fetchall()
        created_matches = []

        for mId in mIds:
            for i in range(len(teams)):
                team1 = teams[i]
                for j in range(i + 1, len(teams)):
                    team2 = teams[j]

                    function2 = 'CreateMatchResult(%s,%s,%s)'
                    cursor.execute(f"SELECT {function2}", (mId, team1, 0))
                    cursor.execute(f"SELECT {function2}", (mId, team2, 0))
                    db.commit()

                    # Fetch the created match results
                    cursor.execute('SELECT * FROM match_results WHERE MID = %s AND TeamID = %s', (mId, team1))
                    result_team1 = cursor.fetchone()
                    created_matches.append(result_team1)

                    cursor.execute('SELECT * FROM match_results WHERE MID = %s AND TeamID = %s', (mId, team2))
                    result_team2 = cursor.fetchone()
                    created_matches.append(result_team2)

        return created_matches

 

    except Exception as e:
        return jsonify({'error': f'Error creating match results: {str(e)}'}), 500

    finally:
        cursor.close()

@app.route('/championship/<int:cId>/draw', methods=['POST'])
def drawChamp(cId):
    try:
        teams = request.json.get('teams', [])

        if not teams:
            return jsonify({'error': 'Teams are NULL'}), 400
        
        cursor = db.cursor()
               
 
        cursor.execute('SELECT COUNT(*) FROM matches WHERE CID = %s', (cId,))
        count = cursor.fetchone()[0]

        if count > 0:
            cursor.execute('DELETE FROM matches WHERE CID = %s', (cId,))
            db.commit()
        
        num_comb =  math.comb(len(teams), 2)
        for _ in range(num_comb):
            function1 = 'CreateMatch(%s,%s,%s)'
 
            cursor.execute(f"SELECT {function1}", ('2023-01-01',    '00:00:00' ,'Location'  ))
            db.commit()
 
        results = matchResult(cId, teams)


 
    except Exception as e:
        return jsonify({'error': f'Error creating drawing champ: {str(e)}'}), 500

    finally:
        db.close()
    return jsonify(results), 200



# Get list of all matches and match results 
@app.route('/championship/<int:cId>/matches', methods=['GET'])
def getMatches(cId):
    try:
  
        cursor = db.cursor()
    
        if sqlInj(cId):
            return jsonify({'error': 'Invalid input detected. SQL injection attempt detected.'}), 400

        
        cursor.execute('''
                        SELECT *
                        FROM matches
                       ''')
        results=cursor.fetchall()
      

 
    except Exception as e:
        return jsonify({'error': f'Error getting matches: {str(e)}'}), 500

    finally:
        cursor.close()
    return jsonify(results)


@app.route('/championship/<int:cId>/matches/<int:mId>', methods=['PUT'])
def updateMatch():
    try:
        mDate = request.json.get('mDate')
        mTime = request.json.get('mTime')
        mLocation = request.json.get('mLocation')

        if sqlInj(mDate, mTime, mLocation):
            return jsonify({'error': 'Invalid input detected. SQL injection attempt detected.'}), 400


        cursor = db.cursor()
        function = 'CreateMatch(%s,%s,%s)'
        cursor.execute(f"SELECT {function}", (mDate, mTime, mLocation))
        db.commit()



 

    except Exception as e:
        return jsonify({'error': f'Error updating matches: {str(e)}'}), 500

    finally:
        cursor.close()
    return 'Success',200

@app.route('/championship/<int:cId>/matches/<int:mId>/matchresults/<int:mrId>', methods=['PUT'])
def updateMR(mId, mrId):
    try:
        mrScore = request.json.get('mrScore')
        if sqlInj(mrId, mId, mrScore):
            return jsonify({'error': 'Invalid input detected. SQL injection attempt detected.'}), 400

        cursor = db.cursor()
        function = 'UpdateMR(%s,%s,%s)'
        cursor.execute(f"SELECT {function}", (mrId, mId, mrScore))
        db.commit()
 
 
    except Exception as e:
        return jsonify({'error': f'Error updating matches: {str(e)}'}), 500

    finally:
        cursor.close()
    return 'Success',200


if __name__ == '__main__':
    app.run(port=5005)