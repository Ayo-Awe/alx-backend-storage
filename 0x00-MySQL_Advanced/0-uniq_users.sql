-- creates a users table with the id,
-- name and email as columns

CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT,
	name VARCHAR(255),
	email VARCHAR(255) NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT users_email_unique UNIQUE (email)
)
