import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="flyway",
    password="flywaypassword",
    database="subscribers"
)
cursor = conn.cursor()

# Check if 'subscribers' table exists
cursor.execute("SHOW TABLES LIKE 'subscribers'")
table_exists = cursor.fetchone()

assert table_exists, "Error: 'subscribers' table does not exist!"

# Check if 'subscription_date' column exists
cursor.execute("SHOW COLUMNS FROM subscribers LIKE 'subscription_date'")
column_exists = cursor.fetchone()

assert column_exists, "Error: 'subscription_date' column is missing!"

print("Schema validation passed!")

conn.close()
