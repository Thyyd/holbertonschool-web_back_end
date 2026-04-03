-- Creates a trigger that resets the attribute valid_email when the email has been changed

-- Create the trigger that will resets the attribute valid_email
DELIMITER $$

CREATE TRIGGER reset_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET valid_email = 0
    END IF;
END$$

DELIMITER;
