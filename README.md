
# Loan Risk Analysis and Borrower Insights

This repository contains the analysis of borrower data with a focus on loan risk, delayed payments, and loan type evaluation. It aims to identify key factors contributing to delayed payments, provide insights into loan amounts, and recommend strategies to mitigate risks for future lending decisions.

## Table of Contents

- [Project Overview](#project-overview)
- [Data](#data)
- [Files in the Repository](#files-in-the-repository)
- [Analysis Highlights](#analysis-highlights)
- [ETL Process](#etl-process)
- [How to Run the Project](#how-to-run-the-project)
- [Recommendations](#recommendations)
- [Contributors](#contributors)

## Project Overview

The goal of this project is to analyze borrower loan data to identify trends, risks, and opportunities for optimizing loan approval criteria. The analysis focuses on delayed payments across different loan types (Auto Loans, Home Loans, and Personal Loans) and how loan amounts correlate with payment delays. Insights gained from this analysis can help lenders make more informed decisions about loan approvals and interventions.

## Data

- **Dataset**: The analysis is based on a dataset of 5,000 borrowers (`5k_borrowers_data.csv`), which includes various borrower attributes such as loan type, loan amount, repayment history, and payment delays.
  
## Files in the Repository

- **`5k_borrowers_data.csv`**: The raw data containing details of 5,000 borrowers including loan amount, loan type, and payment history.
- **`borrowers.db`**: A database file containing the structured borrower data used for querying and analysis.
- **`analysis_queries.sql`**: SQL queries used to perform key analyses, including repayment history, loan amounts, and delayed payments.
- **`analysis_results.txt`**: The results of the analysis queries, highlighting insights into borrower behavior and delayed payments.
- **`preprocessing.ipynb`**: A Jupyter Notebook detailing the preprocessing steps used to clean and prepare the dataset for analysis.
- **`etl_process.py`**: A Python script implementing the ETL (Extract, Transform, Load) process for handling the borrower data.
- **`README.md`**: The readme file that explains the purpose and contents of the repository.

## Analysis Highlights

### Loan Amount Analysis
- The average loan amount across all borrowers is **$55,293.28**.
- Borrowers with delayed payments have an average loan amount of **$55,664.42**, suggesting that higher loan amounts may increase the likelihood of payment delays.

### Top Borrowers
- The highest loan amount is **$99,999**, with a cluster of high-value loans near the **$100,000** mark.
  
### Repayment History
- No borrowers were found with a "Good" repayment history, suggesting the need for clarification or re-categorization of repayment history terminology.

### Loan Type Analysis
- **Personal Loans** have the highest number of delayed payments (873), indicating that they may carry more risk compared to **Home Loans** and **Auto Loans**.

### Delayed Payments
- Approximately **50.08%** of loans have experienced delayed payments, a concerning figure that calls for further investigation into loan approval criteria and borrower support.

## ETL Process

The **`etl_process.py`** script outlines the steps to extract, transform, and load the data into a structured format suitable for analysis. It handles tasks such as:
- Data extraction from the raw `.csv` file.
- Data cleaning and transformation.
- Loading the cleaned data into a database (`borrowers.db`) for analysis.

## How to Run the Project

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Annkkitaaa/Loan-Risk-Analysis-and-Borrower-Insights
   ```

2. Install the required Python libraries:
   ```bash
   pip install pandas sqlite3 jupyter
   ```

3. Run the ETL process:
   ```bash
   python etl_process.py
   ```

4. Open and run the **`preprocessing.ipynb`** notebook to preprocess the data.

5. Execute the SQL queries in **`analysis_queries.sql`** against the **`borrowers.db`** database to generate insights.

## Recommendations

- Investigate the factors contributing to the high rate of delayed payments, especially for **Personal Loans**.
- Review loan approval criteria, particularly for high-value loans, to mitigate risk.
- Develop a clearer system for categorizing repayment history for better tracking and analysis.
- Implement targeted support programs for borrowers with larger loan amounts, as they seem more prone to payment delays.
