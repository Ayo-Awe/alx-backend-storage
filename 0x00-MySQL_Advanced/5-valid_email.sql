--   creates a trigger that decreases the
-- quantity of an item after adding a new order.

delimiter //
CREATE TRIGGER update_check BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;//
delimiter ;
