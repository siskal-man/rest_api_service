import mysql.connector


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="online_store",
        auth_plugin='mysql_native_password'
    )


mycursor = mydb.cursor()

sql = 'SELECT * FROM couriers WHERE regions = "[1, 12, 22]"'

mycursor.execute(sql)

print('courier_id :: courier_type :: regions :: working_hours')
for item in mycursor:
    print(item)
