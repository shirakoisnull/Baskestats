# Baskestats Backend API

> [!IMPORTANT]
>
> - You need a running instance of the [baskestats database](../database/README.md) to run this project. Please follow the instructions in the [baskestats database](../database/README.md) to setup the database.
> - You must also have python3 installed to run this project as this is a flask project.

# Table of Contents

- [Baskestats Backend API](#baskestats-backend-api)
- [Table of Contents](#table-of-contents)
  - [Setup](#setup)
    - [Install dependencies](#install-dependencies)
    - [Run the server](#run-the-server)
    - [OR](#or)
  - [API Endpoints](#api-endpoints)
    - [:5001/login](#5001login)
      - [POST](#post)
        - [Request](#request)
    - [:5002/player](#5002player)
      - [GET](#get)
      - [POST](#post-1)
        - [Request](#request-1)
    - [:5002/player/](#5002player-1)
      - [PUT](#put)
    - [:5002/player/](#5002player-2)
      - [GET](#get-1)
    - [:5002/player/](#5002player-3)
      - [DELETE](#delete)
    - [:5003/team](#5003team)
      - [GET](#get-2)
      - [POST](#post-2)
        - [Request](#request-2)
    - [:5003/team/](#5003team-1)
      - [PUT](#put-1)
      - [GET](#get-3)
      - [DELETE](#delete-1)
    - [:5004/championships](#5004championships)
      - [GET](#get-4)
      - [POST](#post-3)
        - [Request](#request-3)
    - [:5004/championships/](#5004championships-1)
      - [PUT](#put-2)
      - [GET](#get-5)
      - [DELETE](#delete-2)
    - [:5005/championships/draw](#5005championshipsdraw)
      - [POST](#post-4)
        - [Request](#request-4)
    - [:5005/championships//matches](#5005championshipsmatches)
      - [GET](#get-6)
    - [:5005/championships//matches/](#5005championshipsmatches-1)
      - [PUT](#put-3)
    - [:5005/championships//winner](#5005championshipswinner)
      - [GET](#get-7)
    - [:5005/matches//matchresults/](#5005matchesmatchresults)
      - [PUT](#put-4)

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
