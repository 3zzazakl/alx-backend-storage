-- create trigger
CREATE TRIGGER valid_email
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        UPDATE users SET valid_email = 0 WHERE id = NEW.id;
    END IF;
END;
