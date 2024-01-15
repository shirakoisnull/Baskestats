START TRANSACTION;


CREATE TABLE secretary (
    username varchar(255) NOT NULL,
    password varchar(255),
  	PRIMARY KEY (username),
);


CREATE TABLE player (
    PID int NOT NULL AUTO_INCREMENT,
  	TID int,
  	name varchar(255),
  	age int,
  	height int,
  	weight int,
  	pointsscored int,
  	PRIMARY KEY (PID),
    FOREIGN KEY (TID) REFERENCES team(TID)ON DELETE SET NULL
);


CREATE TABLE team (
    TID int NOT NULL AUTO_INCREMENT,
    name varchar(255),
  	city varchar(255),
  	wins int,
  	losses int,
  	PRIMARY KEY (TID)
);


CREATE TABLE championship (
    CID int NOT NULL AUTO_INCREMENT,
    year int,
  	PRIMARY KEY (CID)
);


CREATE TABLE matches (
    MID int NOT NULL AUTO_INCREMENT,
  	CID int,
    matchdate date,
  	matchtime time,
  	location varchar(255),
  	PRIMARY KEY (MID),
  	FOREIGN KEY (CID) REFERENCES championship(CID) ON DELETE CASCADE
);


CREATE TABLE matchresult (
    MRID int NOT NULL AUTO_INCREMENT,
  	MID int,
  	TID int,
    score int,
  	PRIMARY KEY (MRID),
  	FOREIGN KEY (MID) REFERENCES matches(MID) ON DELETE CASCADE,
  	FOREIGN KEY (TID) REFERENCES team(TID)
);


COMMIT;
