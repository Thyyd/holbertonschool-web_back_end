-- Creates a trigger that decrease the quantity of an item after adding a new order

-- Create the trigger that will decrease the quantity of the item
DELIMITER $$

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER;