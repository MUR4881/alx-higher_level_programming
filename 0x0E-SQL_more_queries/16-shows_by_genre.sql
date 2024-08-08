-- Import database dump and fetch column (of a table) by(of) another

-- Import the database dump
-- SOURCE hbtn_0d_tvshow.sql  # Import not needed, Imported when testing

-- list all shows and all genre linked to the show in the database
    SELECT title, name
      FROM tv_show_genres
RIGHT JOIN tv_genres
	ON tv_genres.id = genre_id
RIGHT JOIN tv_shows
	ON tv_shows.id = show_id
  ORDER BY title ASC, name ASC;
