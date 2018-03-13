2. 你可能注意到了，在上一个答案中，有些公司名称存在空格，肯定不适合作为邮箱地址。看看你能否通过删掉客户名称中的所有空格来创建合适的邮箱地址，否则你的答案就和问题 1. 的一样。此处是一些实用的文档。
WITH t1 AS
	(SELECT primary_poc, REPLACE(name, ' ', '') AS name, 
	LEFT(primary_poc, strpos(primary_poc,' ') - 1) AS first_name,
	RIGHT(primary_poc, LENGTH(primary_poc) - strpos(primary_poc,' ')) AS last_name   
FROM accounts)

SELECT first_name, last_name,
	CONCAT (first_name, '.' , last_name, '@', name, '.com' ) AS e_mail
FROM t1
3.我们还需要创建初始密码，在用户第一次登录时将更改。初始密码将是 primary_poc 的名字的第一个字母（小写），然后依次是名字的最后一个字母（小写）、姓氏的第一个字母（小写）、姓氏的最后一个字母（小写）、名字的字母数量、姓氏的字母数量，然后是合作的公司名称（全大写，没有空格）

WITH t1 AS
	(SELECT primary_poc AS poc_name,
	LEFT(primary_poc, strpos(primary_poc,' ') - 1) AS first_name,
	RIGHT(primary_poc, LENGTH(primary_poc) - strpos(primary_poc,' ')) AS last_name,
     REPLACE(name, ' ', '') AS com_name
FROM accounts),
t2 AS
(SELECT  poc_name,
		LOWER(LEFT(first_name, 1)) AS p1, 
		LOWER(RIGHT(first_name, 1)) AS p2,
		LOWER(LEFT(last_name, 1)) AS p3,
		LOWER(RIGHT(last_name, 1)) AS p4, 
        CAST(LENGTH(first_name) AS int) AS p5,
        CAST(LENGTH(last_name) AS int) AS p6,
 		UPPER(com_name) AS p7
FROM t1)
SELECT poc_name , CONCAT(p1,p2,p3,p4,p5,p6,p7)
FROM t2