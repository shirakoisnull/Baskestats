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
        cursor = db.cursor()
        cursor.execute(
            """
                        SELECT player.*, team.name
                        FROM player
                        LEFT JOIN team ON player.TID = team.TID
                        WHERE player.TID IS NOT NULL OR team.TID IS NULL;
                    """
        )
        results = cursor.fetchall()

        cursor.close

    except Exception as e:
        return jsonify({"error": f"Error viewing players: {str(e)}"}), 500

    finally:
        cursor.close()
    return jsonify(results)


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

        # Checking for @ and ! symbols for SQL injection
        if sqlInj(pName, pAge, pHeight, pWeight, pPoints):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        cursor = db.cursor()
        function = "CreatePlayer(%s, %s, %s, %s, %s)"
        cursor.execute(f"SELECT {function}", (pName, pAge, pHeight, pWeight, pPoints))
        db.commit()

    except Exception as e:
        return jsonify({"error": f"Error creating player: {str(e)}"}), 500

    finally:
        cursor.close()
    return "Success", 200


# Associate player with team
@app.route("/associate", methods=["POST"])
def associatePlayerTeam():
    try:
        # Requesting variables
        pId = request.json.get("pId")
        teamId = request.json.get("teamId")
        # Checking for @ and ! symbols for SQL injection
        if sqlInj(pId, teamId):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        cursor = db.cursor()
        function = "AssociatePlayerTeam(%s, %s)"
        cursor.execute(f"SELECT {function}", (pId, teamId))
        db.commit()

    except Exception as e:
        return jsonify({"error": f"Error associating player: {str(e)}"}), 500

    finally:
        cursor.close()
    return "Success", 200


# Update selected player
@app.route("/players/<int:pId>", methods=["PUT"])
def updatePlayer():
    try:
        # Requesting variables
        pName = request.json.get("pName")
        pAge = request.json.get("pAge")
        pHeight = request.json.get("pHeight")
        pWeight = request.json.get("pWeight")
        pPoints = request.json.get("pPoints")
        pId = request.json.get("pId")
        # Checking for @ and ! symbols for SQL injection
        if sqlInj(pName, pAge, pHeight, pWeight, pPoints, pId):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        cursor = db.cursor()
        function = "UpdatePlayer(%s, %s, %s, %s, %s)"
        cursor.execute(
            f"CALL {function}", (pId, pName, pAge, pHeight, pWeight, pPoints)
        )
        db.commit()

    except Exception as e:
        return jsonify({"error": f"Error updating player: {str(e)}"}), 500

    finally:
        cursor.close()
    return "Success", 200


# View player's page
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

        cursor = db.cursor()
        cursor.execute("SELECT * FROM players WHERE PID = %s", (pId))
        result = cursor.fetchone()

    except Exception as e:
        return jsonify({"error": f"Error viewing player: {str(e)}"}), 500

    finally:
        cursor.close()
    return jsonify(result)


# Delete selected player
@app.route("/players/<int:pId>", methods=["DELETE"])
def deletePlayer():
    try:
        pId = request.json.get("pId")
        if sqlInj(pId):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        cursor = db.cursor()
        function = "DeletePlayer(%s)"
        cursor.execute(f"SELECT {function}", ({pId}))
        db.commit()

    except Exception as e:
        return jsonify({"error": f"Error deleting player: {str(e)}"}), 500

    finally:
        cursor.close()
    return "Success", 200


if __name__ == "__main__":
    app.run(port=5002)
