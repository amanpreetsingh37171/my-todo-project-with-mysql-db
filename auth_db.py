import mysql.connector


# conn = mysql.connector.connect(
#     host="localhost",
#     port = 3306,
#     username="root",
#     password="12345",
#     database = "streamlitproject"
# )


conn = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    port=3306,
    user="sql12794129",
    password="rZKbzahu5G",
    database="sql12794129",
)

csr = conn.cursor()