-- Creates a function that divides the first number by the second one and returns 0 if the second number is equal to 0

-- Create the function that divides two numbers
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE Div_res FLOAT DEFAULT 0.0;  -- Déclaration d'une variable temporaire

    IF b != 0 THEN
        -- Fais la division de a par b si b ne vaut pas 0
        SET Div_res = a / b;
    END IF;

	RETURN Div_res;
END //

DELIMITER ;
