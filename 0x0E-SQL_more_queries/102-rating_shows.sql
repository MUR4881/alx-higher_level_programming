-- List all shows by hbtn_0d_tvshows_rate

--  \. hbtn_0d_tvshows_rate.sql  -- <- Remove the 1st 2 chars, to import

-- list all shows by their rating sum
  SELECT title, SUM(rate) AS rating
    FROM tv_shows
    JOIN tv_show_ratings
      ON id = show_id
GROUP BY title
ORDER BY rating DESC;
