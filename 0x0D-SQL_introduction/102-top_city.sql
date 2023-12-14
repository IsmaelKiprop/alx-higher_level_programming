-- List top 3 temperature in July or August
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 8 OR month = 7
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
