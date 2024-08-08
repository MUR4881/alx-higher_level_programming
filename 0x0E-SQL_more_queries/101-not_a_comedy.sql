-- Import database dump and fetch column (of a table) by(of) another

-- Import the database dump
-- SOURCE hbtn_0d_tvshow.sql  # Import not needed, Imported when testing

-- list all NON Comedy show in the database `hbtn_0d_tvshows`
  SELECT title
    FROM tv_shows
  EXCEPT  -- Filtering OF those titles related to Genre comedy
  SELECT title
    FROM tv_show_genres
    JOIN tv_genres
      ON tv_genres.id = genre_id
    JOIN tv_shows
      ON tv_shows.id = show_id
   WHERE name = "Comedy"
ORDER BY title ASC;
