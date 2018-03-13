1.提供每个区域拥有最高销售额 (total_amt_usd) 的销售代表的姓名。
WITH reg_sales_sort_orders AS 
	(SELECT r.name reg_name, s.name sale_name, 
     	SUM(total_amt_usd) sum_total
     FROM orders o
     JOIN accounts a
     ON o.account_id = a.id
     JOIN sales_reps s
     ON a.sales_rep_id = s.id
     JOIN region r
     ON s.region_id = r.id
     GROUP BY 1, 2
     ),
    max_total AS (
	SELECT reg_name max_reg_name, MAX(sum_total) max_total
	FROM reg_sales_sort_orders
	GROUP BY 1
	)
SELECT reg_name, sale_name, sum_total
FROM reg_sales_sort_orders r
JOIN max_total m
ON r.reg_name = m.max_reg_name AND r.sum_total = m.max_total

2.对于具有最高销售额 (total_amt_usd) 的区域，总共下了多少个订单？
Ans: Northeast	1230378
WITH reg_sort_orders AS 
	(SELECT r.name reg_name, 
     	SUM(total_amt_usd) sum_total
     FROM orders o
     JOIN accounts a
     ON o.account_id = a.id
     JOIN sales_reps s
     ON a.sales_rep_id = s.id
     JOIN region r
     ON s.region_id = r.id
     GROUP BY 1
     ), 
     max_total AS
     (SELECT MAX(sum_total) max_total
	 FROM reg_sort_orders
	 )

SELECT  r.name , SUM(o.total) tot
FROM orders o
JOIN accounts a
ON o.account_id = a.id
JOIN sales_reps s
ON a.sales_rep_id = s.id
JOIN region r
ON s.region_id = r.id 
GROUP BY r.name
HAVING SUM(o.total_amt_usd)  = (SELECT * FROM max_total)

5.对于总消费前十名的客户，他们的平均终身消费 (total_amt_usd) 是多少?
304846.969000000000
WITH top_ten AS
	(
	SELECT  a.id, a.name as acc_name, SUM(o.total_amt_usd) AS sum_amt
	FROM orders o
	JOIN accounts a 
	ON o.account_id = a.id
	GROUP BY 1, 2
    ORDER BY 3 DESC
	LIMIT 10
    )
SELECT AVG(sum_amt)

6.比所有客户的平均消费高的企业平均终身消费 (total_amt_usd) 是多少？4721.1397439971747168
WITH account_avg AS(
SELECT a.id AS acc_id, a.name AS acc_name, AVG(total_amt_usd) AS avg_amt
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY 1, 2)



FROM top_ten 