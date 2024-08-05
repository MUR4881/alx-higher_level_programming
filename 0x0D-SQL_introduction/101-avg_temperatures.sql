-- Estimate the average temperature of cities

-- Set context to hbtn_0c_0
USE hbtn_0c_0;

-- Import the TABLE/DATA
\. temperatures.sql

-- Manipulate for average_temp by city and ordering(in descending order) by it
SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	GROUP BY city ORDER BY avg_temp DESC;
