-- Create procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE weight_average_score FLOAT;
    set weight_average_score = (SELECT SUM(weight * score) / SUM(weight) FROM users AS U JOIN corrections AS C ON U.id = C.user_id Join projects AS P ON C.project_id = P.id WHERE U.id = user_id);

    UPDATE users SET average_weighted_score = weight_average_score WHERE id = user_id;

END $$

DELIMITER ;
