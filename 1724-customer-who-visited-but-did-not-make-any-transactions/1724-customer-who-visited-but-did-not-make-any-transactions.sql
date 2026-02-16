# Write your MySQL query statement below
SELECT customer_id, count(customer_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions on Transactions.visit_id = Visits.visit_id
WHERE transaction_id is NULL
GROUP BY customer_id