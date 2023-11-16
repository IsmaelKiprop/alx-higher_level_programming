-- Lists all shows contained in hbtn_0d_tvshows database without genre linked
SELECT tv_shows.title, sg.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres AS sg ON tv_shows.id = sg.show_id
WHERE sg.genre_id is NULL
ORDER BY tv_shows.title, sg.genre_id ASC;
