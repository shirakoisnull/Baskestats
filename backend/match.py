from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
import pymysql
import math
import os
from datetime import datetime, timedelta


# Install requirements with pip install --upgrade -r requirements.txt

app = Flask(__name__)
CORS(app)

load_dotenv()


# (╯°□°)╯︵ ┻━┻
# (╯°□°)╯︵ ┻━┻
# (╯°□°)╯︵ ┻━┻
# (╯°□°)╯︵ ┻━┻
# (╯°□°)╯︵ ┻━┻


db_host = os.environ["DB_HOST"]
db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

# Checking for SQL injections, basically if characters @ and ! in returned values
def sqlInj(*values):
    forbidden_symbols = ["@", "!"]
    for value in values:
        if any(symbol in str(value) for symbol in forbidden_symbols):
            return True
    return False

# Generate the match results for all matches of a championship
def matchResult(cId, teams):
    try:
        with db.cursor() as cursor:
            # Get all the mIds that were previously generated
            cursor.execute("SELECT MID FROM matches WHERE CID = %s", (cId,))
            mIds = cursor.fetchall()
            # Generate all possible team pairs, again, excluding duplicates
            team_pairs = [
                (teams[i], teams[j])
                for i in range(len(teams))
                for j in range(i + 1, len(teams))
            ]
            # For each pair, generate match results instance for each team
            for i, (team1, team2) in enumerate(team_pairs):
                function = "CreateMatchResult(%s,%s,%s)"
                cursor.execute(f"SELECT {function}", (mIds[i][0], team1, 0))
                db.commit()
                cursor.execute(f"SELECT {function}", (mIds[i][0], team2, 0))
                db.commit()
                
    except Exception as e:
        return {"error": f"Error creating match results: {str(e)}"}


# Drawing the latest championship, given a list of teams
@app.route("/championships/draw", methods=["POST"])
def drawChamp():
     
    try:
        with db.cursor() as cursor:
            teams = request.json.get("teams", [])

            if not teams:
                return jsonify({"error": "Teams are NULL"}), 400
            
            # Select the ID of the latest championship
            cursor.execute("SELECT MAX(CID) FROM championship")
            cId = cursor.fetchone()[0]
            # Check to see if matches already exist
            cursor.execute("SELECT COUNT(*) FROM matches WHERE CID = %s", (cId,))
            count = cursor.fetchone()[0]
            # IF they exist, delete them
            if count > 0:
                cursor.execute("DELETE FROM matches WHERE CID = %s", (cId,))

                cursor.execute(
                    "DELETE FROM matchresult WHERE MID IN (SELECT MID FROM matches WHERE CID = %s)",
                    (cId,)
                )
                db.commit()

            # Create new matches based  on current date, each match is one day apart
            current_date = datetime.now().date()
            # Possible number of combinations without duplicates, (team1,team2) and (team2,team1) is the same.
            num_comb = math.comb(len(teams), 2)
            for _ in range(num_comb):
                function1 = "CreateMatch(%s,%s,%s)"
                 
                cursor.execute(
                    f"SELECT {function1}", (current_date, "21:00:00", "Stadium A")
                )

                current_date+=timedelta(days=1)

                db.commit()

            matchResult(cId, teams)

    except Exception as e:
        return jsonify({"error": f"Error creating drawing champ: {str(e)}"}), 500

  
    return 'Success\n', 201


# Get list of all matches and match results
@app.route("/championships/<int:cId>/matches", methods=["GET"])
def getMatches(cId):
    try:
        with db.cursor() as cursor:
            
            if sqlInj(cId):
                return (
                    jsonify(
                        {"error": "Invalid input detected. SQL injection attempt detected."}
                    ),
                    400,
                )

            cursor.execute(
                        """
                            SELECT  matches.MID,
                                    location,
                                    CAST(matchdate AS CHAR) AS matchdate,
                                    CAST(matchtime AS CHAR) AS matchtime,
                                    GROUP_CONCAT(team.name) AS team_names,
                                    GROUP_CONCAT(matchresult.score) AS scores,
                                    GROUP_CONCAT(matchresult.MRID) AS mrid
                                            
                            FROM matches
                            JOIN matchresult ON matches.MID = matchresult.MID
                            JOIN team ON matchresult.TID = team.TID
                            WHERE matches.CID = %s
                            GROUP BY matches.MID, location, matchdate, matchtime;
                        """,
                (cId,),
            )

            results = cursor.fetchall()

    except Exception as e:
        return jsonify({"error": f"Error getting matches: {str(e)}"}), 500
 
    return jsonify(results),200


@app.route("/championships/<int:cId>/matches/<int:mId>", methods=["PUT"])
def updateMatch(cId, mId):
    try:
        mDate = request.json.get("mDate")
        mTime = request.json.get("mTime")
        mLocation = request.json.get("mLocation")

        if sqlInj(mDate, mTime, mLocation):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        with db.cursor() as cursor:
            function = "UpdateMatches(%s,%s,%s,%s)"
            cursor.execute(f"SELECT {function}", (mId, mDate, mTime, mLocation))
            db.commit()

    except Exception as e:
        return jsonify({"error": f"Error updating matches: {str(e)}"}), 500
 
    return "Success\n", 200


@app.route(
    "/championships/<int:cId>/matches/<int:mId>/matchresults/<int:mrId>/<int:tId>",
    methods=["PUT"],
)
def updateMR(cId, mId, mrId, tId):
    try:
        mrScore = request.json.get("mrScore")

        if sqlInj(mrId, mId, mrScore):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        with db.cursor() as cursor:
            function = "UpdateMR(%s,%s,%s,%s)"
            cursor.execute(f"SELECT {function}", (mrId, mId, tId, mrScore))
            db.commit()

    except Exception as e:
        return jsonify({"error": f"Error updating matche results: {str(e)}"}), 500

 
    return "Success\n", 200

@app.route("/championships/<int:cId>/winner", methods=["GET"])
def winner(cId):
    try:
        with db.cursor() as cursor:
            
            if sqlInj(cId):
                return (
                    jsonify(
                        {"error": "Invalid input detected. SQL injection attempt detected."}
                    ),
                    400,
                )
            
            cursor.execute(
                        """
                            SELECT  team.TID, team.name, COUNT(team.TID) AS wins
                                            
                            FROM macthes
                            JOIN matchresult As mr1 ON matches.MID = matchresult.MID
                            JOIN matchresult As mr2 ON matches.MID = matchresult.MID AND mr1.MRID<>mr2.MRID

                            JOIN team ON (mr1.score > mr2.score AND mr1.TID = team.TID) OR (mr1.score < mr2.score AND mr1.TID = team.TID)

                            WHERE matches.CID = %s  
                            GROUD BY wins DESC
                            LIMIT 1;
                        """,
                (cId,),
            )

            result = cursor.fetchone()

    except Exception as e:
        return jsonify({"error": f"Error getting winner: {str(e)}"}), 500
 
    return jsonify(result),200

# Update the score (only) of a single team in a match
@app.route(
    "/matches/<int:mId>/matchresults/<int:mrId>",
    methods=["PUT"],
)
def updateScore(mId, mrId):
    try:
        mrScore = request.json.get("mrScore")

        if sqlInj(mrId, mId, mrScore):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        with db.cursor() as cursor:
            function = "UpdateScore(%s,%s,%s)"
            cursor.execute(f"SELECT {function}", (mrId, mId, mrScore))
            db.commit()

    except Exception as e:
        return jsonify({"error": f"Error updating score: {str(e)}"}), 500

 
    return "Success\n", 200

if __name__ == "__main__":
    app.run(port=5005)
