1.
SELECT *
FROM sf_crime_data
LIMIT 10;
4.
SELECT incidnt_num, 
		date, 
		CONCAT(SUBSTR(date,7,4),'-',SUBSTR(date, ) ,'-', SUBSTR(3,2))
FROM sf_crime_data