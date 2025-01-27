-- Drop tigger
-- DROP TRIGGER IF EXISTS update_item_quantity;

-- Create trigger
CREATE TRIGGER update_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
