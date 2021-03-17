from mysql import connector


def insert_data(data: list):
    mydb = connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="online_store",
        auth_plugin='mysql_native_password'
    )

    cursor = mydb.cursor()

    sql = "INSERT INTO couriers (courier_id, courier_type, regions, working_hours) VALUES (%s, %s, %s, %s)"

    cursor.execute(sql, [*data])

    mydb.commit()


def update_data(data: list):
    pass