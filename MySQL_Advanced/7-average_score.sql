-- Creates a procedure that computes and stores the average score for a student.

-- Create the procedure that will compute and store the average score of a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT     -- Correspondance à users.id
)
BEGIN
    DECLARE user_id_exists INT DEFAULT 0;  -- Déclaration d'une variable temporaire
    DECLARE user_average_score FLOAT;  -- Déclaration d'une variable temporaire pour la moyenne

    -- Vérification si l'user existe
    SELECT COUNT(*) INTO user_id_exists  -- Stocke l'id dans user_id_exists
    FROM users
    WHERE id = user_id;

    IF user_id_exists = 0 THEN
        -- Soulève une erreur car l'user n'existe pas
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'User not found';
    END IF;

    -- Calcul de la moyenne et stockage de celle-ci dans users.average_score

    -- AVG(score) calcule la moyenne des scores
    SELECT AVG(score) INTO user_average_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = user_average_score
    WHERE id = user_id;
END //

DELIMITER ;
