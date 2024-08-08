-- Show rating sum by genres for all genres
-- source hbtn_0d_tvshows_rate  -- removes the 1st --'s to import the db dump

-- Show genres by rating
  SELECT name, SUM(rate) AS rating	-- name only relate to genre
    FROM tv_show_genres
    JOIN tv_genres			-- Join tv_genres to t_s_g
      ON genre_id = tv_genres.id
    JOIN tv_shows			-- Join tv_show to the prev comb
      ON show_id = tv_shows.id
    JOIN tv_show_ratings
      ON tv_show_ratings.show_id = tv_shows.id	-- Join ratings to prev comb
GROUP BY name	-- The whole comb (table) get arranged by name (genre name)
ORDER BY rating DESC;
