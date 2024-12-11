-- Create procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight INT DEFAULT 0
    DECLARE weighted_sum FLOAT DEFAULT 0

    SELECT SUM (c.score * p.weight) INTO weighted_sum, SUM (p.weight) INTO total_weight FROM correction C
    JOIN projects p On c.project_id = p.id
    WHERE c.user_id = user_id;

    IF total_weight > 0 THEN
        UPDATE users SET average_weighted_score = (weighted_sum / total_weight) WHERE id = user_id;
    ELSE
        UPDATE users SET average_weighted_score = 0 WHERE id = user_id;
    END IF;
END$$

DELIMITER ;
