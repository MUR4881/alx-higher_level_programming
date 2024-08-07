-- Import database dump and fetch column (of a table) by(of) another

-- Import the database dump
-- SOURCE hbtn_0d_tvshow.sql  # Import not needed, Imported when testing

-- list all shows contained in hbtn_0d_tvshows that with their genre_id
   SELECT title, genre_id
     FROM tv_shows
LEFT JOIN tv_show_genres  -- Basically LEFT OUTER JOIN
       ON id = show_id
 ORDER BY title ASC, genre_id ASC;
