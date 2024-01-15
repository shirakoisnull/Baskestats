# Baskestats Backend API

> [!IMPORTANT]
> - You need a running instance of the [baskestats database](../database/README.md) to run this project. Please follow the instructions in the [baskestats database](../database/README.md) to setup the database.
> - You must also have python3 installed to run this project as this is a flask project.


## Setup

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
python run_backend.py
```

### OR
(if you have a linux machine with tmux installed)

```bash
chmod +x start_backend.sh && ./start_backend.sh
```

## API Endpoints

### :5001/login

#### POST

##### Request

```json
{
  "username": "username",
  "password": "password"
}
```

### :5002/player

#### GET

Get list of all players, returns PlayerID, TeamID, name, age, height, weight, pointsscored in this order. If team is none, null is returned.

#### POST

Create a new player

##### Request

```json
{
  "name": "name",
  "age": "age",
  "height": "height",
  "weight": "weight",
  "pointsscored": "pointsscored",
  "teamid": "teamid"
}
```

### :5002/player/<playerid>

#### PUT

Update a player

### :5002/player/<playerid>

#### GET

Get a player by id

### :5002/player/<playerid>

#### DELETE

Delete a player by id

### :5003/team

#### GET

Get list of all teams, returns TeamID, name, city, state, country, sport in this order.

#### POST

Create a new team

##### Request

```json
{
  "name": "name",
  "city": "city",
  "wins": "wins",
  "losses": "losses"
}
```

### :5003/team/<teamid>

#### PUT

Update a team

#### GET

Get a team by id

#### DELETE

Delete a team by id

### :5004/championships

#### GET

Get list of all championships, returns ChampionshipID, name, year in this order.

#### POST

Create a new championship

##### Request

```json
{
  "name": "name",
  "year": "year"
}
```

### :5004/championships/<championshipid>

#### PUT

Update a championship

#### GET

Get a championship by id

#### DELETE

Delete a championship by id

### :5005/championships/draw

#### POST

Draw the latest championship, given a list of teams

##### Request

```json
{
  "teams": ["teamid1", "teamid2", "teamid3", "teamid4"]
}
```

### :5005/championships/<championshipid>/matches

#### GET

Get list of all matches and match results in a championship, returns MatchID, Match Location, Match Date, Match Time, "Team1Name, Team2Name", "Team1Score, Team2Score", "MatchResultID1, MatchResultID2" in this order.

### :5005/championships/<championshipid>/matches/<matchid>

#### PUT

Update a match (match date, match time, match location)

### :5005/championships/<championshipid>/winner

#### GET

Get the winner of a championship

### :5005/matches/<matchid>/matchresults/<matchresultid>

#### PUT

Update a team's score in a match
