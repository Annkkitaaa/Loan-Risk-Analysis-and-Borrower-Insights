import pandas as pd
import sqlite3

# Step 1: Data Extraction
file_path = r"C:\Users\Ankita Singh\assigmentfordataengineer\5k_borrowers_data.csv"
try:
    borrowers_df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"CSV file not found at the provided path: {file_path}")
    exit(1)

# Print column names
print("Original column names:")
print(borrowers_df.columns)

# Print first few rows
print("\nFirst few rows of the data:")
print(borrowers_df.head())

# Step 2: Data Transformation
# Cleaning and standardizing the data
borrowers_df.columns = [col.strip().lower().replace(' ', '_') for col in borrowers_df.columns]
borrowers_df.fillna('', inplace=True)

# Print column names after transformation
print("\nColumn names after transformation:")
print(borrowers_df.columns)

# Step 3: Data Loading
# Creating SQLite database and table
conn = sqlite3.connect('borrowers.db')
cursor = conn.cursor()

# Drop the table if it exists
cursor.execute("DROP TABLE IF EXISTS borrowers")

# Create the table
cursor.execute('''
CREATE TABLE borrowers (
    name TEXT,
    date_of_birth TEXT,
    gender TEXT,
    marital_status TEXT,
    phone_number TEXT,
    email_address TEXT,
    mailing_address TEXT,
    language_preference TEXT,
    geographical_location TEXT,
    credit_score REAL,
    loan_type TEXT,
    loan_amount REAL,
    loan_term TEXT,
    interest_rate REAL,
    loan_purpose TEXT,
    emi REAL,
    ip_address TEXT,
    geolocation TEXT,
    repayment_history TEXT,
    days_left_to_pay_current_emi INTEGER,
    delayed_payment TEXT
)
''')

# Loading data into the database
borrowers_df.to_sql('borrowers', conn, if_exists='replace', index=False)

print("\nETL process completed successfully.")

# Function to execute query and print results
def execute_query(query, description):
    print(f"\n{description}")
    try:
        result = pd.read_sql_query(query, conn)
        print(result)
    except Exception as e:
        print(f"Error executing query: {e}")

# Query to check table structure
execute_query("PRAGMA table_info(borrowers);", "Table structure:")

# Query a: Average loan amount for borrowers with delayed payment
query_a = """
SELECT AVG(loan_amount) AS average_loan_amount 
FROM borrowers 
WHERE delayed_payment = 'Yes';
"""
execute_query(query_a, "a. Average loan amount for borrowers with delayed payment:")

# Query b: Top 10 borrowers with highest loan amount
query_b = """
SELECT name, loan_amount 
FROM borrowers 
ORDER BY loan_amount DESC 
LIMIT 10;
"""
execute_query(query_b, "b. Top 10 borrowers with highest loan amount:")

# Query c: Borrowers with good repayment history
query_c = """
SELECT * 
FROM borrowers 
WHERE repayment_history = 'Good';
"""
execute_query(query_c, "c. Borrowers with good repayment history:")

# Query d: Analysis with respect to loan type
query_d = """
SELECT loan_type, 
       COUNT(*) AS number_of_borrowers, 
       AVG(loan_amount) AS average_loan_amount, 
       AVG(CAST(days_left_to_pay_current_emi AS INTEGER)) AS average_days_left_to_pay,
       SUM(CASE WHEN delayed_payment = 'Yes' THEN 1 ELSE 0 END) AS delayed_payments_count
FROM borrowers 
GROUP BY loan_type;
"""
execute_query(query_d, "d. Analysis with respect to loan type:")

# Close the connection
conn.close()

print("\nAll queries executed.")