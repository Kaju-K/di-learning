SELECT *
FROM customer;

SELECT (first_name, last_name) AS full_name
FROM customer;

SELECT DISTINCT create_date 
FROM customer;

SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate DESC;

SELECT address, phone
FROM address
WHERE 
	(district = 'Texas');
	
SELECT *
FROM film
WHERE 
	(film_id IN (15, 150));

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE 
	(title ILIKE 'batman%');
	
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE 
	(title ILIKE 'ba%');
	
SELECT *
FROM film
ORDER BY 
	rental_rate ASC,
	title ASC
LIMIT 10;

SELECT *
FROM film
ORDER BY 
	rental_rate ASC,
	title ASC
LIMIT 10
OFFSET 10;

SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
INNER JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

SELECT *
FROM inventory
WHERE 
	(store_id = 2);
	
SELECT city.city, country.country
FROM city
LEFT JOIN country
ON city.country_id = country.country_id;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
INNER JOIN payment p
ON c.customer_id = p.customer_id
ORDER BY staff_id ASC