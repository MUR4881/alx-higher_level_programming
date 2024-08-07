-- Import database dump and fetch column (of a table) by(of) another

-- Import the database dump
-- SOURCE hbtn_0d_tvshow.sql  # Import not needed, Imported when testing

-- list all shows contained in hbtn_0d_tvshows without genre linked
   SELECT title, genre_id
     FROM tv_shows
LEFT JOIN tv_show_genres  -- Basically LEFT OUTER JOIN
       ON id = show_id
    WHERE genre_id IS NULL  -- FILTERING FOR SHOWS WITH NO genre
 ORDER BY title ASC,
       genre_id ASC;
