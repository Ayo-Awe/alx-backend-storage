-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.

delimiter //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	DECLARE weighted_avg FLOAT DEFAULT 0;

	SELECT (SUM(p.weight * c.score ) / SUM(p.weight)) INTO weighted_avg
	FROM corrections c
	JOIN projects p ON c.project_id = p.id
	WHERE c.user_id = user_id;

	UPDATE users SET average_score = weighted_avg WHERE users.id = user_id;
END;//
delimiter ;
