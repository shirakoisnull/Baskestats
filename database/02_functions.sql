DELIMITER //


CREATE FUNCTION CreateTeam(team_name VARCHAR(255), team_city VARCHAR(255), team_wins INT, team_losses INT)
RETURNS INT
BEGIN
    DECLARE team_id INT;

    INSERT INTO team (name, city, wins, losses) 
    VALUES (team_name, team_city, team_wins, team_losses);

    SET team_id = LAST_INSERT_ID();

    RETURN team_id;
END //


CREATE FUNCTION CreatePlayer(
    player_name VARCHAR(255),
    player_age INT,
    player_height INT,
    player_weight INT,
    player_pointsscored INT
)
RETURNS INT
BEGIN
    DECLARE player_id INT;

    INSERT INTO player (name, age, height, weight, pointsscored) 
    VALUES (player_name, player_age, player_height, player_weight, player_pointsscored);

    SET player_id = LAST_INSERT_ID();

    RETURN player_id;
END //


CREATE FUNCTION CreatePlayer(
    player_name VARCHAR(255),
    player_age INT,
    player_height INT,
    player_weight INT,
    player_pointsscored INT
)
RETURNS INT
BEGIN
    DECLARE player_id INT;

    INSERT INTO player (name, age, height, weight, pointsscored) 
    VALUES (player_name, player_age, player_height, player_weight, player_pointsscored);

    SET player_id = LAST_INSERT_ID();

    RETURN player_id;
END //


CREATE FUNCTION CreateChampionship(champ_year INT)
RETURNS INT
BEGIN
    DECLARE champ_id INT;

    INSERT INTO championship (year) 
    VALUES (champ_year);

    SET champ_id = LAST_INSERT_ID();

    RETURN champ_id;
END //


CREATE FUNCTION CreateMatch(match_date DATE, match_time TIME, match_location VARCHAR(255))
RETURNS INT
BEGIN
    DECLARE match_id INT;

    INSERT INTO matches(matchdate, matchtime, location, CID) 
    VALUES (match_date, match_time, match_location, (SELECT MAX(CID) FROM championship));

    SET match_id = LAST_INSERT_ID();

    RETURN match_id;
END //


CREATE FUNCTION CreateMatchResult(match_id INT,team_id INT,mr_score INT)
RETURNS INT
BEGIN
    DECLARE mr_id INT;
		
    INSERT INTO matchresult (MID,TID,score) 
    VALUES (match_id,team_id,mr_score);

    SET mr_id = LAST_INSERT_ID();

    RETURN mr_id;
END //


CREATE FUNCTION AssociatePlayerTeam(player_id INT, team_id INT)
RETURNS INT
BEGIN
    UPDATE player 
    SET TID = team_id 
    WHERE PID = player_id;

    RETURN player_id;
END //


CREATE FUNCTION UpdateTeam(team_id INT, team_name VARCHAR(255), team_city VARCHAR(255), team_wins INT, team_losses INT)
RETURNS BOOLEAN
BEGIN
    DECLARE rows_affected INT;

    UPDATE team 
    SET 
        name = team_name, 
        city = team_city, 
        wins = team_wins, 
        losses = team_losses
    WHERE 
        TID = team_id;

    SET rows_affected = ROW_COUNT();

    IF rows_affected > 0 THEN
        RETURN TRUE; -- Update successful
    ELSE
        RETURN FALSE; -- No rows updated (team_id not found)
    END IF;
END //


CREATE FUNCTION UpdatePlayer(player_id INT, player_name VARCHAR(255),player_age INT,player_height INT,player_weight INT,player_pointsscored INT)
RETURNS BOOLEAN
BEGIN
    DECLARE rows_affected INT;

    UPDATE player
    SET 
        name = player_name, 
        age = player_age, 
        height = player_height, 
        weight = player_weight,
        pointsscored = player_pointsscored
    WHERE 
        PID = player_id;

    SET rows_affected = ROW_COUNT();

    IF rows_affected > 0 THEN
        RETURN TRUE; -- Update successful
    ELSE
        RETURN FALSE; -- No rows updated (team_id not found)
    END IF;
END //


CREATE FUNCTION UpdateSecretary(secretary_name VARCHAR(255), secretary_password INT)
RETURNS BOOLEAN
BEGIN
    DECLARE rows_affected INT;

    UPDATE secretary
    SET 
        username = secretary_name, 
        password = secretary_password
        
    WHERE 
        username = secretary_name;

    SET rows_affected = ROW_COUNT();

    IF rows_affected > 0 THEN
        RETURN TRUE; -- Update successful
    ELSE
        RETURN FALSE; -- No rows updated (team_id not found)
    END IF;
END //


CREATE FUNCTION UpdateChampionship(championship_id INT, championship_year INT)
RETURNS BOOLEAN
BEGIN
    DECLARE rows_affected INT;

    UPDATE championship
    SET 
        year = championship_year
    WHERE 
        CID = championship_id;

    SET rows_affected = ROW_COUNT();

    IF rows_affected > 0 THEN
        RETURN TRUE; -- Update successful
    ELSE
        RETURN FALSE; -- No rows updated (team_id not found)
    END IF;
END //


CREATE FUNCTION UpdateMatches(match_id INT, match_date DATE,match_time TIME,match_location VARCHAR(255))
RETURNS BOOLEAN
BEGIN
    DECLARE rows_affected INT;

    UPDATE matches
    SET 
        matchdate = match_date,
        matchtime = match_time,
        location = match_location
    WHERE 
        MID = match_id;

    SET rows_affected = ROW_COUNT();

    IF rows_affected > 0 THEN
        RETURN TRUE; -- Update successful
    ELSE
        RETURN FALSE; -- No rows updated (team_id not found)
    END IF;
END //


CREATE FUNCTION UpdateMR(mr_id INT, match_id INT,team_id INT,mr_score INT)
RETURNS BOOLEAN
BEGIN
    DECLARE rows_affected INT;

    UPDATE matchresult
    SET 
        MID = match_id,
        TID = team_id,
        score = mr_score
    WHERE 
        MRID = mr_id;

    SET rows_affected = ROW_COUNT();

    IF rows_affected > 0 THEN
        RETURN TRUE; -- Update successful
    ELSE
        RETURN FALSE; -- No rows updated (team_id not found)
    END IF;
END //

CREATE FUNCTION UpdateScore (
  mr_id INT,
  match_id INT,
  mr_score INT
) RETURNS tinyint(1) BEGIN DECLARE rows_affected INT;

UPDATE
  matchresult
SET
  score = mr_score
WHERE
  MRID = mr_id AND MID = match_id;

SET
  rows_affected = ROW_COUNT();

IF rows_affected > 0 THEN
RETURN
  TRUE;

 -- Update successful
ELSE
RETURN
  FALSE;

END IF;

END
	
CREATE FUNCTION DeleteTeam(row_id INT)
RETURNS INT
BEGIN
    DECLARE row_selected INT;

    DELETE FROM team WHERE TID = row_id;
    SET row_selected = ROW_COUNT();

    RETURN row_selected;
END //


CREATE FUNCTION DeletePlayer(row_id INT)
RETURNS INT
BEGIN
    DECLARE row_selected INT;

    DELETE FROM player WHERE PID = row_id;
    SET row_selected = ROW_COUNT();

    RETURN row_selected;
END //


CREATE FUNCTION DeleteChampionship(row_id INT)
RETURNS INT
BEGIN
    DECLARE row_selected INT;

    DELETE FROM championship WHERE CID = row_id;
    SET row_selected = ROW_COUNT();

    RETURN row_selected;
END //


CREATE FUNCTION DeleteSecretary(row_id VARCHAR(255))
RETURNS INT
BEGIN
    DECLARE row_selected INT;

    DELETE FROM secretary WHERE username = row_id;
    SET row_selected = ROW_COUNT();

    RETURN row_selected;
END //


CREATE FUNCTION DeleteMatch(row_id INT)
RETURNS INT
BEGIN
    DECLARE row_selected INT;

    DELETE FROM matches WHERE MID = row_id;
    SET row_selected = ROW_COUNT();

    RETURN row_selected;
END //


CREATE FUNCTION DeleteMR(row_id INT)
RETURNS INT
BEGIN
    DECLARE row_selected INT;

    DELETE FROM matchresult WHERE MRID = row_id;
    SET row_selected = ROW_COUNT();

    RETURN row_selected;
END //


DELIMITER ;
