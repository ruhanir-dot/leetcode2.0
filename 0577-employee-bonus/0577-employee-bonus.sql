# Write your MySQL query statement below
SELECT name, bonus 
FROM Employee as e
left join Bonus as b
on e.empId = b.empId
WHERE
   bonus is NULL OR bonus < 1000
Order by name ASC

