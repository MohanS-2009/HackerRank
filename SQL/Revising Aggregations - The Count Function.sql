/* 

Query a count of the number of cities in CITY having a Population larger than .

*/

SELECT count(DISTRICT) AS cities
FROM CITY
WHERE Population > 100000;