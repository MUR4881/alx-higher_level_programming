-- List all cities of California that can be found in table city db hbtn_0d_usa
SELECT id, name
  FROM cities
 WHERE state_id
    IN
      (SELECT id
	 FROM states
	WHERE name = "California")
ORDER BY cities.id
