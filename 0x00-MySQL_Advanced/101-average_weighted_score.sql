-- Create procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_weight INT;
    DECLARE weighted_sum FLOAT;
    DECLARE done INT DEFAULT 0;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT SUM(c.score * p.weight), SUM(p.weight) INTO weighted_sum, total_weight
            FROM corrections AS c
            JOIN projects AS p ON c.project_id=p.id
            WHERE c.user_id=user_id;

            if total_weight = 0 then
                UPDATE users SET average_score = weighted_sum / total_weight
                WHERE id=user_id;
            ELSE
                UPDATE users SET average_score = 0 WHERE id=user_id;
            END IF;
        END LOOP;
        CLOSE cur;

END $$

DELIMITER ;
