1. 
SELECT primary_poc, 
LEFT(primary_poc, POSITION(' ' IN primary_poc)) AS first_name, 
RIGHT(primary_poc, LENGTH(primary_poc) - POSITION(' ' IN primary_poc)) AS last_name
FROM accounts
GROUP BY 1
ORDER BY 1;