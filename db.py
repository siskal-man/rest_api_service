import mysql.connector


def insert_data_courier(data: list):
    mydb = mysql.connector.connect(
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


def update_data_courier(courier_id, data: dict):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="online_store",
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()

    if len(data) == 1:
        if 'courier_type' in data.keys():
            sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
            val = (str(data['courier_type']), courier_id)

            mycursor.execute(sql, val)

            mydb.commit()
        elif 'regions' in data.keys():
            sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
            val = (str(data['regions']), courier_id)

            mycursor.execute(sql, val)

            mydb.commit()
        elif 'working_hours' in data.keys():
            sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
            val = (str(data['working_hours']), courier_id)

            mycursor.execute(sql, val)

            mydb.commit()

    elif len(data) == 2:
        if 'courier_type' in data.keys():
            if 'regions' in data.keys():
                sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
                val = (str(data['courier_type']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
                val = (str(data['regions']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
            elif 'working_hours' in data.keys():
                sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
                val = (str(data['courier_type']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
                val = (str(data['working_hours']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
        elif 'working_hours' in data.keys():
            if 'regions' in data.keys():
                sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
                val = (str(data['working_hours']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
                val = (str(data['regions']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
            elif 'courier_type' in data.keys():
                sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
                val = (str(data['working_hours']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
                val = (str(data['courier_type']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
        elif 'regions' in data.keys():
            if 'courier_type' in data.keys():
                sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
                val = (str(data['regions']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
                val = (str(data['courier_type']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()
            elif 'working_hours' in data.keys():
                sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
                val = (str(data['regions']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

                sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
                val = (str(data['working_hours']), courier_id)

                mycursor.execute(sql, val)
                mydb.commit()

    elif len(data) == 3:
        sql = "UPDATE couriers SET regions = %s WHERE courier_id = %s"
        val = (str(data['regions']), courier_id)

        mycursor.execute(sql, val)
        mydb.commit()

        sql = "UPDATE couriers SET working_hours = %s WHERE courier_id = %s"
        val = (str(data['working_hours']), courier_id)

        mycursor.execute(sql, val)
        mydb.commit()

        sql = "UPDATE couriers SET courier_type = %s WHERE courier_id = %s"
        val = (str(data['courier_type']), courier_id)

        mycursor.execute(sql, val)
        mydb.commit()


def insert_data_order(data: list):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="online_store",
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO orders (order_id, weight, region, delivery_hours) VALUES (%s, %s, %s, %s)"

    mycursor.execute(sql, [*data])

    mydb.commit()

