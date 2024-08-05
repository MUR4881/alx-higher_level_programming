-- Estimate the average temperature of cities
-- temperatures is expected to have been imported
-- Manipulate for average_temp by city and ordering(in descending order) by it
SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	GROUP BY city ORDER BY avg_temp DESC;
