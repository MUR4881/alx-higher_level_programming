-- lists the number of records with the same score
-- A table of the score alongside the number of times
SELECT score, COUNT(score) AS number FROM second_table
	GROUP BY score ORDER BY number DESC;
