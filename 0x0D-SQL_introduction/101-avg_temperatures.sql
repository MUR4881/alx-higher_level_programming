-- Estimate the average temperature of cities

-- Import the TABLE/DATA
SOURCE temperatures.sql;

-- Manipulate for average_temp by city and ordering(in descending order) by it
SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	GROUP BY city ORDER BY avg_temp DESC;
