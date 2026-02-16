# Write your MySQL query statement below
SElECT unique_id, name
FROM Employees 
LEFT JOIN EmployeeUNI on EmployeeUNI.id = Employees.id
