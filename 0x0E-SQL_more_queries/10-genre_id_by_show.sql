-- Lists all shows contained in hbtn_0d_tvshows database that have at least one genre linked
SELECT s.title, sg.genre_id
FROM tv_shows AS s
JOIN tv_show_genres AS sg ON s.id = sg.show_id 
JOIN tv_genres AS g ON g.id = sg.genre_id
ORDER BY s.title, sg.genre_id ASC;
