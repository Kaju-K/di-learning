SELECT * FROM students;

SELECT first_name, last_name FROM students;

SELECT first_name, last_name
FROM students
WHERE
	(id = 2);

SELECT first_name, last_name
FROM students
WHERE
	(last_name = 'Benichou')
	AND
	(first_name = 'Marc');
	
SELECT first_name, last_name
FROM students
WHERE
	(last_name = 'Benichou')
	OR
	(first_name = 'Marc');
	
SELECT first_name, last_name
FROM students
WHERE
	(first_name ILIKE '%a%');
	
SELECT first_name, last_name
FROM students
WHERE
	(first_name ILIKE 'a%');
	
SELECT first_name, last_name
FROM students
WHERE
	(first_name ILIKE '%a');

SELECT first_name, last_name
FROM students
WHERE
	(first_name ILIKE '_%a%_');
	
SELECT first_name, last_name
FROM students
WHERE
	(id = 1)
	AND
	(id = 3);
	
SELECT *
FROM students
WHERE
	(birth_date >= '1/01/2000')