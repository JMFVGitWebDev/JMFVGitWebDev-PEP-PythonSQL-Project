import csv
import os
import sqlite3

# Resolve the resources folder relative to this file, so paths work
# no matter what directory the script is run from.
_RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'resources')

# Connect to the SQLite in-memory database
conn = sqlite3.connect(':memory:')

# A cursor object to execute SQL commands
cursor = conn.cursor()


def main():

    # users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        userId INTEGER PRIMARY KEY,
                        firstName TEXT,
                        lastName TEXT
                      )'''
                   )

    # callLogs table (with FK to users table)
    cursor.execute('''CREATE TABLE IF NOT EXISTS callLogs (
        callId INTEGER PRIMARY KEY,
        phoneNumber TEXT,
        startTime INTEGER,
        endTime INTEGER,
        direction TEXT,
        userId INTEGER,
        FOREIGN KEY (userId) REFERENCES users(userId)
    )''')

    # You will implement these methods below. They just print TO-DO messages for now.
    load_and_clean_users(os.path.join(_RESOURCES_DIR, 'users.csv'))
    load_and_clean_call_logs(os.path.join(_RESOURCES_DIR, 'callLogs.csv'))
    write_user_analytics(os.path.join(_RESOURCES_DIR, 'userAnalytics.csv'))
    write_ordered_calls(os.path.join(_RESOURCES_DIR, 'orderedCalls.csv'))

    # Helper method that prints the contents of the users and callLogs tables. Uncomment to see data.
    # select_from_users_and_call_logs()

    # Close the cursor and connection. main function ends here.
    cursor.close()
    conn.close()


# TODO: Implement the following 4 functions. The functions must pass the unit tests to complete the project.


# This function will load the users.csv file into the users table, discarding any records with incomplete data
def load_and_clean_users(file_path):

    #print(file_path)

    with open('/home/ubuntu/JMFVGitWebDev-PEP-PythonSQL-Project/resources/users.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        try:
            header = next(reader)
        except StopIteration:
            header = []  # or handle empty file case (e.g., raise a custom message or skip)
            print("The CSV file is empty.") #header = next(reader)  # Skip the header row if present

        clean_records = []
        id_number = 0
        for row in reader:
            # Discard records with missing columns or empty strings/None values
            if len(row) != len(header) or (not(all(cell.strip() for cell in row))):
                #row.insert(0, id_number)
                id_number = id_number + 1
                clean_records.append(row)
        
        #print(clean_records)
        # Create placeholders (?, ?, ...) based on column count
        placeholders = ', '.join(['?'] * 3)
        #cursor.executemany(f"INSERT INTO users VALUES ({placeholders})", clean_records)
        insert_sql = f"INSERT INTO users VALUES ({placeholders})"

        #print(insert_sql)

        #query = "INSERT INTO users VALUES (%s, %s, %s)"

        #for params in clean_records:
        #    formatted_query = query % params  # or use .format() / f-strings depending on syntax
        #    print(formatted_query)


        for row in clean_records:
            cursor.execute(insert_sql, row)

        cursor.execute('''SELECT * FROM users''') 

        results = cursor.fetchall()
        num_records = len(results)
        print(num_records)

        rows = cursor.fetchall()

        # 3. Loop through and print each row
        #for row in rows:
            #print(row)   

    # Commit changes and close the connection
    conn.commit()
    #conn.close()

    print("TODO: load_users")


# This function will load the callLogs.csv file into the callLogs table, discarding any records with incomplete data
def load_and_clean_call_logs(file_path):

    print("TODO: load_call_logs")


# This function will write analytics data to testUserAnalytics.csv - average call time, and number of calls per user.
# You must save records consisting of each userId, avgDuration, and numCalls
# example: 1,105.0,4 - where 1 is the userId, 105.0 is the avgDuration, and 4 is the numCalls.
def write_user_analytics(csv_file_path):

    print("TODO: write_user_analytics")


# This function will write the callLogs ordered by userId, then start time.
# Then, write the ordered callLogs to orderedCalls.csv
def write_ordered_calls(csv_file_path):

    print("TODO: write_ordered_calls")



# No need to touch the functions below!------------------------------------------

# This function is for debugs/validation - uncomment the function invocation in main() to see the data in the database.
def select_from_users_and_call_logs():

    print()
    print("PRINTING DATA FROM USERS")
    print("-------------------------")

    # Select and print users data
    cursor.execute('''SELECT * FROM users''')
    for row in cursor:
        print(row)

    # new line
    print()
    print("PRINTING DATA FROM CALLLOGS")
    print("-------------------------")

    # Select and print callLogs data
    cursor.execute('''SELECT * FROM callLogs''')
    for row in cursor:
        print(row)


def return_cursor():
    return cursor


if __name__ == '__main__':
    main()