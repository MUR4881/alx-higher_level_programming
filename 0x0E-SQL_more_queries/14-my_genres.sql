-- Import database dump and fetch column (of a table) by(of) another

-- Import the database dump
-- SOURCE hbtn_0d_tvshow.sql  # Import not needed, Imported when testing

-- list all genres of the show Dexter
  SELECT name
    FROM tv_show_genres
    JOIN tv_genres
      ON tv_genres.id = genre_id
    JOIN tv_shows
      ON tv_shows.id = show_id
   WHERE title = "Dexter"
ORDER BY name;
