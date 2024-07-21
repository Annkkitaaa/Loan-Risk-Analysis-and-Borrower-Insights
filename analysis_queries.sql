-- a. What is the average loan amount for borrowers who are more than 5 days past due?
SELECT AVG(loan_amount) AS average_loan_amount
FROM borrowers
WHERE due_days > 5;

-- b. Who are the top 10 borrowers with the highest outstanding balance?
SELECT name, outstanding_balance
FROM borrowers
ORDER BY outstanding_balance DESC
LIMIT 10;

-- c. List of all borrowers with good repayment history
SELECT * FROM borrowers
WHERE repayment_history = 'good';

-- d. Brief analysis wrt loan type
SELECT loan_type, COUNT(*) AS number_of_borrowers, AVG(loan_amount) AS average_loan_amount, AVG(outstanding_balance) AS average_outstanding_balance
FROM borrowers
GROUP BY loan_type;

-- e. Average Loan Amount for Borrowers More Than 5 Days Past Due
SELECT AVG(Loan Amount) AS average_loan_amount
FROM borrowers
WHERE `Days Left to Pay Current EMI` <= 0;

--f. Top 10 Borrowers with the Highest Outstanding Balance
SELECT Name, Outstanding Balance
FROM borrowers
ORDER BY Outstanding Balance DESC
LIMIT 10;

--g. List of All Borrowers with Good Repayment History
SELECT * 
FROM borrowers
WHERE `Repayment History` = 'good';

--h. Brief Analysis by Loan Type
SELECT `Loan Type`, 
       COUNT(*) AS number_of_borrowers, 
       AVG(`Loan Amount`) AS average_loan_amount, 
       AVG(`Outstanding Balance`) AS average_outstanding_balance
FROM borrowers
GROUP BY `Loan Type`;

--i. Average Credit Score by Marital Status
SELECT `Marital Status`, 
       AVG(`Credit Score`) AS average_credit_score
FROM borrowers
GROUP BY `Marital Status`;

--j. Total Loan Amount Disbursed by Geographical Location
SELECT `Geographical Location`, 
       SUM(`Loan Amount`) AS total_loan_amount_disbursed
FROM borrowers
GROUP BY `Geographical Location`;

--k. Borrowers with High Interest Rates and Their Contact Information
SELECT Name, 
       `Phone Number`, 
       `Email Address`, 
       `Loan Amount`, 
       `Interest Rate`
FROM borrowers
WHERE `Interest Rate` > 10;

--l. Distribution of Loan Amounts by Loan Purpose
SELECT `Loan Purpose`, 
       COUNT(*) AS number_of_borrowers, 
       AVG(`Loan Amount`) AS average_loan_amount
FROM borrowers
GROUP BY `Loan Purpose`;
