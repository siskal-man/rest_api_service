from mysql import connector


def insert_data(data: list):
    mydb = connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="online_store",
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO couriers (courier_id, courier_type, regions, working_hours) VALUES (%s, %s, %s, %s)"

    mycursor.execute(sql, [*data])

    mydb.commit()


# TODO: сделать проверку ключей
def update_data(courier_id, data: dict):
    mydb = connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="online_store",
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()

    if len(data) == 1:
        if data[0] == 'courier_type':
            sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
            val = (data[0], courier_id)

            mycursor.execute(sql, val)

            mydb.commit()
        elif data[0] == 'regions':
            sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
            val = (str(data[0]), courier_id)

            mycursor.execute(sql, val)

            mydb.commit()
        elif data[0] == 'working_hours':
            sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
            val = (str(data[0]), courier_id)

            mycursor.execute(sql, val)

            mydb.commit()

    elif len(data) == 2:
        if data[0] == 'courier_type':
            if data[1] == 'regions':
                sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
                val = (data[0], courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
                val = (str(data[1]), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
            elif data[1] == 'working_hours':
                sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
                val = (data[0], courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
                val = (str(data[1]), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
        elif data[0] == 'working_hours':
            if data[1] == 'regions':
                sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
                val = (str(data[0]), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
                val = (str(data[1]), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
            elif data[1] == 'courier_type':
                sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
                val = (str(data[0]), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
                val = (data[1], courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
        elif data[0] == 'regions':
            if data[1] == 'courier_type':
                sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
                val = (data[0], courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
                val = (str(data[1]), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
            elif data[1] == 'working_hours':
                sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
                val = (data[0], courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
                val = (str(data[1]), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

    elif len(data) == 3:
        pass
