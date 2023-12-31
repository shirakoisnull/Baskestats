from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
import pymysql
import math
import os


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


def sqlInj(*values):
    forbidden_symbols = ["@", "!"]
    for value in values:
        if any(symbol in str(value) for symbol in forbidden_symbols):
            return True
    return False


def matchResult(cId, teams):
    cursor = db.cursor()
    try:
        cursor.execute("SELECT MID FROM matches WHERE CID = %s", (cId,))
        mIds = cursor.fetchall()

        team_pairs = [
            (teams[i], teams[j])
            for i in range(len(teams))
            for j in range(i + 1, len(teams))
        ]
        i = 0

        for team1, team2 in team_pairs:
            function = "CreateMatchResult(%s,%s,%s)"
            cursor.execute(f"SELECT {function}", (mIds[i], team1, 0))
            db.commit()
            cursor.execute(f"SELECT {function}", (mIds[i], team2, 0))
            db.commit()

            i += 1

        cursor.execute("SELECT * FROM matchresult")
        match_results = cursor.fetchall()
        return match_results

    except Exception as e:
        print(f"Error: {str(e)}")
        return "Error"

    finally:
        cursor.close()


@app.route("/championships/<int:cId>/draw", methods=["POST"])
def drawChamp(cId):
    cursor = db.cursor()
    try:
        teams = request.json.get("teams", [])

        if not teams:
            return jsonify({"error": "Teams are NULL"}), 400

        cursor.execute("SELECT COUNT(*) FROM matches WHERE CID = %s", (cId,))
        count = cursor.fetchone()[0]

        if count > 0:
            cursor.execute("DELETE FROM matches WHERE CID = %s", (cId,))

            cursor.execute(
                "DELETE FROM matchresult WHERE MID IN (SELECT MID FROM matches WHERE CID = %s)",
                (cId,),
            )
            db.commit()

        num_comb = math.comb(len(teams), 2)
        for _ in range(num_comb):
            function1 = "CreateMatch(%s,%s,%s)"

            cursor.execute(
                f"SELECT {function1}", ("2023-01-01", "00:00:00", "Location")
            )

            db.commit()

        results = matchResult(cId, teams)

    except Exception as e:
        return jsonify({"error": f"Error creating drawing champ: {str(e)}"}), 500

    finally:
        cursor.close()
    return jsonify(results), 200


# Get list of all matches and match results
@app.route("/championships/<int:cId>/matches", methods=["GET"])
def getMatches(cId):
    try:
        cursor = db.cursor()

        if sqlInj(cId):
            return (
                jsonify(
                    {"error": "Invalid input detected. SQL injection attempt detected."}
                ),
                400,
            )

        cursor.execute(
            """
                        SELECT matches.MID, location,
                        CAST(matchdate AS CHAR) AS matchdate,
                        CAST(matchtime AS CHAR) AS matchtime,
                        matchresult.MRID,
                        matchresult.TID, 
                        matchresult.score
                      
                        FROM matches
                        LEFT JOIN matchresult ON matches.MID = matchresult.MID
                        WHERE matches.CID = %s;
                       """,
            (cId,),
        )

        results = cursor.fetchall()

    except Exception as e:
        return jsonify({"error": f"Error getting matches: {str(e)}"}), 500

    finally:
        cursor.close()
    return jsonify(results)


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

        cursor = db.cursor()
        function = "UpdateMatches(%s,%s,%s,%s)"
        cursor.execute(f"SELECT {function}", (mId, mDate, mTime, mLocation))
        db.commit()

    except Exception as e:
        return jsonify({"error": f"Error updating matches: {str(e)}"}), 500

    finally:
        cursor.close()
    return "Success", 200


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

        cursor = db.cursor()
        function = "UpdateMR(%s,%s,%s,%s)"
        cursor.execute(f"SELECT {function}", (mrId, mId, tId, mrScore))
        db.commit()

    except Exception as e:
        return jsonify({"error": f"Error updating matches: {str(e)}"}), 500

    finally:
        cursor.close()
    return "Success", 200


if __name__ == "__main__":
    app.run(port=5005)
