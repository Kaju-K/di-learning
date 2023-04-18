-- UPDATE film
-- SET language_id = (SELECT language_id from language where name = 'German')
-- WHERE 
-- 	title ILIKE '%ba%'

-- SELECT COUNT(*) FROM rental where return_date is null

-- SELECT r.rental_id, p.amount
-- FROM rental r
-- JOIN payment p
-- ON r.rental_id = p.rental_id
-- WHERE return_date IS NULL
-- ORDER BY amount DESC
-- LIMIT 30

-- SELECT ft.title, ft.description, a.first_name, a.last_name
-- FROM film ft
-- JOIN film_actor fa
-- ON ft.film_id = fa.film_id
-- JOIN actor a
-- ON fa.actor_id = a.actor_id
-- WHERE 
-- 	a.first_name = 'Penelope'
-- 	AND
-- 	a.last_name = 'Monroe'
-- 	AND
-- 	ft.description ILIKE '%sumo%'

-- SELECT ft.title, ft.length, ft.rating, c.name
-- FROM film ft
-- JOIN film_category fc
-- ON ft.film_id = fc.film_id
-- JOIN category c
-- ON fc.category_id = c.category_id
-- WHERE 
-- 	length < 60
-- 	AND 
-- 	c.name = 'Documentary'
-- 	AND
-- 	ft.rating = 'R'

-- SELECT DISTINCT f.title, ct.first_name, ct.last_name, p.amount, r.return_date
-- FROM customer ct
-- JOIN payment p
-- ON ct.customer_id = p.customer_id
-- JOIN rental r
-- ON ct.customer_id = r.customer_id
-- JOIN inventory i
-- ON r.inventory_id = i.inventory_id
-- JOIN film f
-- ON i.film_id = f.film_id
-- WHERE 
-- 	ct.first_name = 'Matthew'
-- 	AND
-- 	ct.last_name = 'Mahan'
-- 	AND
-- 	p.amount > 4
-- 	AND
-- 	r.return_date BETWEEN '28-07-2005' AND '01-08-2005'

