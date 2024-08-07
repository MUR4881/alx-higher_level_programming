-- Import database dump and fetch column (of a table) by(of) another

-- Import the database dump
-- SOURCE hbtn_0d_tvshow.sql  # Import not needed, Imported when testing

-- list all shows contained in hbtn_0d_tvshows that have atleast one genre link
  SELECT title, genre_id
    FROM tv_shows
    JOIN tv_show_genres
      ON id = show_id
ORDER BY title ASC, genre_id ASC;
