/* 

Query the average population of all cities in CITY where District is California.

*/

SELECT AVG(POPULATION) AS AVG_POPULATION
FROM CITY

WHERE DISTRICT = 'CALIFORNIA'

