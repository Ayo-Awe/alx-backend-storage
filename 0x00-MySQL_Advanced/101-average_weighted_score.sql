-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.

delimiter //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
	DECLARE weighted_avg FLOAT DEFAULT 0;

	INSERT INTO users (id, name, average_score)
			(SELECT	c.user_id AS id,
					u.name,
					(SUM(p.weight * c.score ) / SUM(p.weight)) AS  average_score
			FROM corrections c
			JOIN projects p ON c.project_id = p.id
			JOIN users u ON c.user_id = u.id
			GROUP BY c.user_id)
	ON DUPLICATE KEY UPDATE average_score = VALUES(average_score);
END;//
delimiter ;
