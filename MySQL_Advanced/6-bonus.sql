-- Creates a procedure that adds a new correction for a student

-- Create the procedure that will add a new correction for a student
DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INT,                 -- Correspondance à users.id
    IN project_name VARCHAR(255),   -- Correspondance à projects.name
    IN score INT                    -- Le score du projet
)
BEGIN
    DECLARE project_id INT;  -- Déclaration d'une variable temporaire

    -- Vérification si le projet existe
    SELECT id INTO project_id  -- Stocke l'id dans project_id
    FROM projects
    WHERE name = project_name;

    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);  -- Ajout du nom du projet dans projects
        SET project_id = LAST_INSERT_ID();  -- Récupération de l'ID du dernier objet créé dans project_id
    END IF;

    -- Ajout de la correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //

DELIMITER ;

