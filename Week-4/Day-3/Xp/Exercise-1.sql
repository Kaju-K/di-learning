-- SELECT * FROM language;

-- SELECT f.title, f.description, l.name 
-- FROM film f
-- FULL OUTER JOIN language l
-- ON f.language_id = l.language_id;

-- CREATE TABLE new_film(
-- 	id SERIAL PRIMARY KEY,
-- 	name TEXT NOT NULL
-- )

-- INSERT INTO new_film (name)
-- VALUES 
-- 	('Batman'),
-- 	('Titanic'),
-- 	('Se Eu Fosse Você')

-- CREATE TABLE customer_review (
-- 	review_id SERIAL primary key NOT NULL,
-- 	film_id int REFERENCES new_film (id) ON DELETE CASCADE,
-- 	language_id int REFERENCES language ON DELETE SET NULL,
-- 	title VARCHAR(50) NOT NULL,
-- 	score INT NOT NULL,
-- 	review_text TEXT,
-- 	last_update DATE NOT NULL
-- )

-- INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update)
-- VALUES
-- 	(
-- 		(SELECT id FROM new_film WHERE name = 'Titanic'),
-- 		(SELECT language_id FROM language WHERE name = 'English'),
-- 		'Why Rose didn''t let Jack get on top of the wood??',
-- 		7,
-- 		'I mean, the movie is nice, I cried a lot, but WTF!! There was enough place for Jack and Rose to be on top of the wood, they both could get out alive. Like, after everything they went through!! Hate it...',
-- 		'14-03-2015'
-- 	),
-- 	(
-- 		(SELECT id FROM new_film WHERE name = 'Se Eu Fosse Você'),
-- 		null,
-- 		'Best thing i have ever seen',
-- 		10,
-- 		'Amazing! Really funny, 10/10',
-- 		'18-04-2023'
-- 	)

-- DELETE FROM new_film WHERE name = 'Se Eu Fosse Você'

SELECT * from customer_review