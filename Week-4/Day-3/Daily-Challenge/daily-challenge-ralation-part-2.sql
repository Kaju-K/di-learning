-- CREATE TABLE book (
-- 	book_id SERIAL PRIMARY KEY,
-- 	title VARCHAR(100) NOT NULL,
-- 	author VARCHAR(100) NOT NULL
-- )

-- INSERT INTO book (title, author)
-- VALUES
-- 	('Alice In Wonderland', 'Lewis Carroll'),
-- 	('Harry Potter', 'J.K Rowling'),
-- 	('To kill a mockingbird', 'Harper Lee')

-- CREATE TABLE student (
-- 	student_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(100) NOT NULL UNIQUE,
-- 	age smallint NOT NULL CHECK(age<=15)
-- )

-- INSERT INTO student (name, age)
-- VALUES
-- 	('John', 12),
-- 	('Lera', 11),
-- 	('Patrick', 10),
-- 	('Bob', 14)

-- CREATE TABLE library (
-- 	book_fk_id INT REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	student_fk_id INT REFERENCES student (student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	borrowed_date DATE NOT NULL
-- )

-- INSERT INTO library (student_fk_id, book_fk_id, borrowed_date)
-- VALUES
-- 	(
-- 		(SELECT student_id FROM student WHERE name = 'John'),
-- 		(SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
-- 		'15-02-2022'
-- 	),
-- 	(
-- 		(SELECT student_id FROM student WHERE name = 'Bob'),
-- 		(SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
-- 		'03-03-2021'
-- 	),
-- 	(
-- 		(SELECT student_id FROM student WHERE name = 'Lera'),
-- 		(SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
-- 		'23-05-2021'
-- 	),
-- 	(
-- 		(SELECT student_id FROM student WHERE name = 'Bob'),
-- 		(SELECT book_id FROM book WHERE title = 'Harry Potter'),
-- 		'12-08-2021'
-- 	)

-- SELECT * FROM library

-- SELECT s.name, b.title
-- FROM student s
-- JOIN library l
-- ON s.student_id = l.student_fk_id
-- JOIN book b
-- ON l.book_fk_id = b.book_id

-- SELECT CAST(AVG(s.age) AS DECIMAL(10,2))
-- FROM student s
-- JOIN library l
-- ON s.student_id = l.student_fk_id
-- JOIN book b
-- ON l.book_fk_id = b.book_id
-- WHERE b.title ILIKE 'Alice%'

-- DELETE FROM student WHERE name = 'Lera'

-- SELECT * FROM library