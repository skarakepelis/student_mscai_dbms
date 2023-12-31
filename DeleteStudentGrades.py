import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('db.sqlite3')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Deleting records
cursor.execute('''DELETE FROM home_studentgrades''')

# Retrieving data after delete
print("All GRADES deleted successfully!")
cursor.execute("SELECT * from home_studentgrades")
print(cursor.fetchall())

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
