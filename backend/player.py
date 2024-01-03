from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
import pymysql
import os

# Install requirements with pip install --upgrade -r requirements.txt

app = Flask(__name__)
CORS(app)

load_dotenv()
db_host = os.environ["DB_HOST"]
db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)


def sqlInj(*values):
    forbidden_symbols = ["@", "!"]
    for value in values:
        if any(symbol in str(value) for symbol in forbidden_symbols):
            return True
    return False


# Get list of all players
@app.route("/players", methods=["GET"])
def getPlayers():
    try:
        with db.cursor() as cursor:
            cursor.execute(
                        """SELECT * FROM player"""
            )
            results = cursor.fetchall()
        

    except Exception as e:
        return jsonify({"error": f"Error viewing players: {str(e)}"}), 500

 
       
    return jsonify(results), 200


# Create new player
@app.route("/players", methods=["POST"])
def createPlayer():
    try:
        # Requesting variables
        pName = request.json.get("pName")
        pAge = request.json.get("pAge")
        pHeight = request.json.get("pHeight")
        pWeight = request.json.get("pWeight")
        pPoints = request.json.get("pPoints")
        teamId = request.json.get("teamId")
 


        # Checking for @ and ! symbols for SQL injection
        if sqlInj(pName, pAge, pHeight, pWeight, pPoints, teamId):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        with db.cursor() as cursor:
            function = "CreatePlayer(%s, %s, %s, %s, %s)"
            
            cursor.execute(f"SELECT {function} AS player_id", (pName, pAge, pHeight, pWeight, pPoints))
            result = cursor.fetchone()

            db.commit()
        
    
            

            if teamId is not None:
                

                function = "AssociatePlayerTeam(%s, %s)"
                cursor.execute(f"SELECT {function}", (result[0], teamId))
                db.commit()
 
    except Exception as e:
        return jsonify({"error": f"Error creating player: {str(e)}"}), 500
 
        
    return "Success\n", 201

  
 
 

# Update selected player
@app.route("/players/<int:pId>", methods=["PUT"])
def updatePlayer(pId):
    try:
        # Requesting variables
        pName = request.json.get("pName")
        pAge = request.json.get("pAge")
        pHeight = request.json.get("pHeight")
        pWeight = request.json.get("pWeight")
        pPoints = request.json.get("pPoints")
        teamId = request.json.get("teamId")
        # Checking for @ and ! symbols for SQL injection
        if sqlInj(pName, pAge, pHeight, pWeight, pPoints, pId, teamId):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )       
        with db.cursor() as cursor:
            if teamId is not None:
                function = "AssociatePlayerTeam(%s, %s)"
                cursor.execute(f"SELECT {function}", (result[0], teamId))
                db.commit()

            
            function = "UpdatePlayer(%s, %s, %s, %s, %s, %s)"
            cursor.execute(
                f"SELECT {function}", (pId, pName, pAge, pHeight, pWeight, pPoints)
            )
            db.commit()
     

    except Exception as e:
        return jsonify({"error": f"Error updating player: {str(e)}"}), 500

  
        
    return "Success\n", 200


#Get player
@app.route("/players/<int:pId>", methods=["GET"])
def viewPlayer():
    try:
        pId = request.json.get("pId")
        if sqlInj(pId):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        with db.cursor() as cursor:
            cursor.execute('''SELECT * FROM players 
                            
                            WHERE PID = %s ''', (pId))
            result = cursor.fetchone()
       

    except Exception as e:
        return jsonify({"error": f"Error viewing player: {str(e)}"}), 500

 
        
    return jsonify(result), 200


# Delete selected player
@app.route("/players/<int:pId>", methods=["DELETE"])
def deletePlayer(pId):
    try:
 
        if sqlInj(pId):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        with db.cursor() as cursor:
            function = "DeletePlayer(%s)"
            cursor.execute(f"SELECT {function}", ({pId}))
            db.commit()
      

    except Exception as e:
        return jsonify({"error": f"Error deleting player: {str(e)}"}), 500

    
        
    return "Success\n", 200


if __name__ == "__main__":
    app.run(port=5002)
