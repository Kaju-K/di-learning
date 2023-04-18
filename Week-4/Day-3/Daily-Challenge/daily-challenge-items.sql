-- CREATE TABLE product_orders (
-- 	id serial primary key,
-- 	date timestamp not null default CURRENT_TIMESTAMP
-- );

-- CREATE TABLE items (
-- 	id serial primary key,
-- 	price int not null,
-- 	name varchar(100) not null unique,
-- 	product_id int references product_orders (id) ON DELETE RESTRICT
-- );

-- INSERT INTO product_orders (date)
-- VALUES 
-- 	(DEFAULT),
-- 	(DEFAULT),
-- 	(DEFAULT),
-- 	(DEFAULT),

-- INSERT INTO items (price, name, product_id)
-- VALUES
-- 	(3, 'pencil', 1),
-- 	(3, 'pen', 1),
-- 	(10, 'notebook', 1),
-- 	(2000, 'laptop', 2),
-- 	(100, 'mouse', 2),
-- 	(60, 'shirt', 3),
-- 	(30, 'rubber duck', 3),
-- 	(50, 'short', 3),
-- 	(150, 'shoes', 3)

CREATE OR REPLACE FUNCTION total_price (order_id int)
RETURNS INT AS
$$
BEGIN
	RETURN (
		SELECT SUM(i.price)
		FROM product_orders p
		JOIN items i
		ON p.id = i.product_id
		WHERE p.id = order_id
	);
END
$$
LANGUAGE plpgsql;

SELECT * FROM total_price(3)
