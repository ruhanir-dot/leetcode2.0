# Write your MySQL query statement below
SELECT w1.id
FROM Weather as w1 # w1 is our copy today records, w2 is our copy we will use for yesterdays 
JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 # For each row in w1 find row in w2 where date difference is 1 date
WHERE w1.temperature > w2.temperature
