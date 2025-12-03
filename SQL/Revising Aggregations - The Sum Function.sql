/* 

Query the total population of all cities in CITY where District is California.

*/

SELECT sum(population) as Total_Population
FROM CITY
WHERE District = 'California'