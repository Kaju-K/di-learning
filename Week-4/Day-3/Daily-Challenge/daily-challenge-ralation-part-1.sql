-- CREATE TABLE customer (
-- 	id serial PRIMARY KEY,
-- 	first_name VARCHAR(50),
-- 	last_name VARCHAR(100) NOT NULL
-- )

-- CREATE TABLE customer_profile (
-- 	id serial PRIMARY KEY,
-- 	isLoggedIn boolean DEFAULT false NOT NULL,
-- 	customer_id int REFERENCES customer (id) ON DELETE CASCADE NOT NULL
-- )

-- INSERT INTO customer (first_name, last_name)
-- VALUES
-- 	('John', 'Doe'),
-- 	('Jerome', 'Lalu'),
-- 	('John', 'Rive')

-- INSERT INTO customer_profile (isLoggedIn, customer_id)
-- VALUES
-- 	(true, (SELECT id FROM customer WHERE first_name = 'John')),
-- 	(DEFAULT, (SELECT id FROM customer WHERE first_name = 'Jerome'))

-- SELECT c.first_name, cp.isloggedin
-- FROM customer_profile cp
-- JOIN customer c
-- ON cp.customer_id = c.id

-- SELECT c.first_name, cp.isloggedin
-- FROM customer_profile cp
-- RIGHT JOIN customer c
-- ON cp.customer_id = c.id

-- SELECT COUNT(c.first_name), cp.isloggedin
-- FROM customer_profile cp
-- RIGHT JOIN customer c
-- ON cp.customer_id = c.id
-- GROUP BY cp.isloggedin
-- HAVING cp.isloggedin = false