INSERT INTO users (id, name, average_score)
		(SELECT	c.user_id AS id,
				u.name,
				(SUM(p.weight * c.score ) / SUM(p.weight)) AS  average_score
		FROM corrections c
		JOIN projects p ON c.project_id = p.id
		JOIN users u ON c.user_id = u.id
		GROUP BY c.user_id)
ON DUPLICATE KEY UPDATE average_score = VALUES(average_score);
