-- Create procedure
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE weight_average_score FLOAT;
    SET weight_average_score = (
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections AS c
        JOIN projects AS p ON c.project_id=p.id
        JOIN users AS u ON c.user_id=u.id
        WHERE u.id=user_id
    );
    
    UPDATE users SET average_score = weight_average_score WHERE id=user_id;

END
$$
DELIMITER ;
