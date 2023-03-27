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
    TTL_TYPE VARCHAR(50)
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
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE) VALUES ('En lair', 'Relsca', 199, 'Hip-hop Sentimental');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE) VALUES ('Je suis trop little', 'Hamza', 214, 'Rap RnB');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE) VALUES ('Je rase Poutine', 'Fiak', 175, 'Drill VNR');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE) VALUES ('Salut swipe up!', 'Niouininho', 179, 'Rap Commercial');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE) VALUES ('Grrr Paw', 'Gazoil', 225, 'Rap Onomatopé');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE) VALUES ('Nous sommes le monde', 'Michael Klaxon', 234, 'Pop payarde');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE) VALUES ('Concerto n° 3 guitare', 'STEUB', 201, 'Cover');
INSERT INTO TITLE_TTL (TTL_NAME, TTL_ARTIST, TTL_DURATION, TTL_TYPE) VALUES ('3 bandes organisé', 'Adidas', 185, 'Rap Marseillais');

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