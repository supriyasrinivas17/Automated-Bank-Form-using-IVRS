import sqlite3

# connecting to the database
connection = sqlite3.connect("accounts_db.db")
crsr = connection.cursor()

# Create table if it doesn't exist
sql_command = """
CREATE TABLE IF NOT EXISTS accounts (
    acc_num VARCHAR(11) PRIMARY KEY,
    name VARCHAR(50),
    branch VARCHAR(50)
);
"""
crsr.execute(sql_command)

# Insert data commands (insert or replace to avoid duplicates)
insert_commands = [
    ('08985438536', 'Streak', 'VSKP'),
    ('12345678901', 'John Doe', 'DEL'),
    ('23456789012', 'Jane Smith', 'MUM'),
    ('34567890123', 'Bob Johnson', 'BLR'),
    ('45678901234', 'Alice Williams', 'HYD'),
    ('56789012345', 'Mike Brown', 'KOL'),
    ('67890123456', 'Sarah Davis', 'CHN'),
    ('78901234567', 'David Wilson', 'PUN'),
    ('89012345678', 'Karen Taylor', 'JAIP'),
    ('90123456789', 'Mark Thompson', 'LUCK'),
    ('01234567890', 'Emily Garcia', 'AHM'),
    ('30217353705', 'Mr. Venkateswarlu Shirly', 'BALANAGAR') 
]

for acc_num, name, branch in insert_commands:
    crsr.execute("INSERT OR REPLACE INTO accounts (acc_num, name, branch) VALUES (?, ?, ?)", (acc_num, name, branch))

connection.commit()

# Print all rows to verify
crsr.execute("SELECT * FROM accounts")
rows = crsr.fetchall()
for row in rows:
    print(row)

connection.close()
