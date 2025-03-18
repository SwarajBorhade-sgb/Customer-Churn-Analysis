
-- Find total number of customers who churned
SELECT COUNT(*) AS Churned_Customers FROM churn_data WHERE Churn = 'Yes';

-- Find average monthly charges for churned vs. non-churned customers
SELECT Churn, AVG(MonthlyCharges) AS Avg_Monthly_Charges FROM churn_data GROUP BY Churn;

-- Find churn rate by gender
SELECT Gender, COUNT(*) AS Total_Customers, 
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers, 
       (SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS Churn_Rate
FROM churn_data GROUP BY Gender;

-- Find customers at high risk of churn (high monthly charges, low tenure)
SELECT CustomerID, Age, MonthlyCharges, Tenure FROM churn_data 
WHERE MonthlyCharges > 80 AND Tenure < 12;
