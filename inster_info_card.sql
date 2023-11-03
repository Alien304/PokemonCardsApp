-- Active: 1697285249220@@127.0.0.1@5432@pokemoncards
ALTER TABLE card
ADD COLUMN Expansion VARCHAR(255);
INSERT INTO set (setid, setname, totalcards, img_url)
VALUES (3, 'SWSH08', 78, 'main_SWSH08.png')

Alter Table set
ADD column img_url VARCHAR;

DELETE FROM SET
WHERE setid >= 2

UPDATE set
SET img_url = 'main_sv01.png'
WHERE setid = 1;