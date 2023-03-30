
---------------------------------------------------------
---------------------------------------------------------
-------------------  CREATE TABLE -----------------------
---------------------------------------------------------
---------------------------------------------------------

CREATE TABLE IF NOT EXISTS USER_USR
(
    ID_USR INTEGER PRIMARY KEY AUTOINCREMENT,
    USR_USERNAME VARCHAR(100),
    USR_MAIL VARCHAR(100),
    USR_PASSWORD VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS TITLE_TTL
(
    ID_TTL INTEGER PRIMARY KEY AUTOINCREMENT,
    TTL_NAME VARCHAR(100),
    TTL_ARTIST VARCHAR(50),
    TTL_DURATION INTEGER,
    TTL_TYPE VARCHAR(50),
    TTL_IMG VARCHAR(120)
);

CREATE TABLE IF NOT EXISTS LIKE_USER_LUS
(
    ID_LUS INTEGER PRIMARY KEY AUTOINCREMENT,

    ID_TTL INTEGER,
    ID_USR INTEGER,

    FOREIGN KEY (ID_TTL) REFERENCES TITLE_TTL,
    FOREIGN KEY (ID_USR) REFERENCES USER_USR
);

---------------------------------------------------------
---------------------------------------------------------
--------------------  INSERT INTO -----------------------
---------------------------------------------------------
---------------------------------------------------------

-- INSERT DATA IN USER_USR TABLE
INSERT INTO USER_USR (USR_USERNAME, USR_MAIL, USR_PASSWORD) VALUES ('Maxime Ancelin', 'maxime.ancelin1@ipilyon.net', '1234');
INSERT INTO USER_USR (USR_USERNAME, USR_MAIL, USR_PASSWORD) VALUES ('Viksha-Alix Gladines', 'vikshaalix.gladines@ipilyon.net', '1234');
INSERT INTO USER_USR (USR_USERNAME, USR_MAIL, USR_PASSWORD) VALUES ('Matthieu Vilmen', 'matthieu.vilmen@ipilyon.net', '1234');

-- INSERT DATA IN TITLE_TTL TABLE
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE, TTL_IMG) VALUES ('En lair', 'Relsca', 199, 'Hip-Hop', 'https://i.scdn.co/image/ab67616d00001e026dec83fcfb43f0d97b0e464d');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE, TTL_IMG) VALUES ('Fixette - Bonus', 'Ziak', 214, 'Drill', 'https://i.scdn.co/image/ab67616d0000b273409c5540246461d5fc587ae5');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE, TTL_IMG) VALUES ('Sadio (feat. Offset)', 'Hamza', 175, 'Rap', 'https://i.scdn.co/image/ab67616d00001e029117ac8cf4dafbf733e9f1d0');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE, TTL_IMG) VALUES ('Désenchantée', 'Mylène Farmer', 179, 'Pop', 'https://i.scdn.co/image/ab67616d00001e02c01f5670830f5ea89856e36c');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE, TTL_IMG) VALUES ('Je te promets', 'Johnny Hallyday', 225, 'Rock FR', 'https://i.scdn.co/image/ab67616d0000b273d3edafddbd98b60f0df346aa');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE, TTL_IMG) VALUES ('Billie Jean', 'Michael Jackson', 234, 'Pop US', 'https://i.scdn.co/image/ab67616d0000b273de437d960dda1ac0a3586d97');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE, TTL_IMG) VALUES ('Animals', 'Martin Garrix', 201, 'Dancefloor', 'https://i.scdn.co/image/ab67616d00001e026abad6915a2216dc18e7e3a7');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE, TTL_IMG) VALUES ('Highway to Hell', 'AC/DC', 185, 'Heavy Metal', 'https://i.scdn.co/image/ab67616d00001e0251c02a77d09dfcd53c8676d0');

-- INSERT DATA IN LIKE_USER_LUS TABLE
INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (1, 1);
INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (1, 4);
INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (1, 5);
INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (2, 8);
INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (2, 5);
INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (2, 2);
INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (3, 2);
INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (3, 3);
INSERT INTO LIKE_USER_LUS (ID_USR, ID_TTL) VALUES (3, 5);