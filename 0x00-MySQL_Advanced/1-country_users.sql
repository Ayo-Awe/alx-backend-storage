-- creates a users table with the id,
-- name, country and email as columns

CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT,
	name VARCHAR(255),
	email VARCHAR(255) NOT NULL,
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY (id),
	CONSTRAINT users_email_unique UNIQUE (email)
)
