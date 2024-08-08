-- Import database dump and fetch column (of a table) by(of) another

-- Import the database dump
-- SOURCE hbtn_0d_tvshow.sql  # Import not needed, Imported when testing

-- list all genres by number of shows
  SELECT name AS genre, count(show_id) AS number_of_shows
    FROM tv_show_genres
    JOIN tv_genres
      ON id = genre_id
GROUP BY name		-- Here it happens, Grouping the biglist by name on tv_genres
ORDER BY number_of_shows DESC;
