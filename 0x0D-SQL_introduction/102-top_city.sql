-- Calculate the top the city with highest average temperature
-- in the month of JULY and August

SELECT city, AVG(value) AS avg_temp FROM temperatures
	WHERE month=7 OR month=8
	GROUP BY city ORDER BY avg_temp DESC
	LIMIT 3;
