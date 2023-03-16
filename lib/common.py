import pymssql

# Tool to define logging information methods and
# all other common methods like helper functions
# used within the program

# Global Function for logging information to file
def log_info(logger_id, timestamp, error_message, update_desc, writefile):
    
    writefile.write("Logger_ID: " + logger_id + ", Timestamp: " + timestamp + ", Error Message: " + error_message + ", Update Description: " + update_desc)

# Helper method to calculate distance between two strings in terms of length    
def difference_between_two_strings(str1, str2):
    return len(str1) - len(str2)
    
# connect to database and return connection
def connect_to_db(server, database, username, password):
    try:
        conn = pymssql.connect(server = server, database = database, user = username, password = password)
        return conn
    except:
        return "Connection Failed, throw error"

# validate a json token
def validate_jwt_token(jwt_token):
    if (jwt_token == "all good"):
        return True
    return False

# insert data into db
def insert_data(data, conn):
    cursor = conn.cursor()
    try:
        cursor.insert(data)
        return "inserted"
    except:
        return "failed"