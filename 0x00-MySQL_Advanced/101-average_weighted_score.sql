-- Create procedure
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users as U,
    (SELECT U.id, SUM(score * weight) / SUM(weight) AS weighted_score
    from users as U
    join corrections as C on U.id=C.user_id
    join projects as P on C.project_id=P.id
    group by U.id) as WA
    SET U.average_score = WA.weighted_score
    WHERE U.id=WA.id;

END
$$
DELIMITER ;



