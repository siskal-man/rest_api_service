from mysql import connector
from pprint import pprint
from datetime import datetime

mydb = connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="online_store",
        auth_plugin='mysql_native_password'
    )

mycursor = mydb.cursor()

sql = "SELECT * FROM couriers"
sql2 = "SELECT * FROM orders"
mycursor.execute(sql)

couriers = mycursor.fetchall()

mycursor.execute(sql2)
orders = mycursor.fetchall()


pprint(couriers)
print('---------------------------------------')
pprint(orders)
print('---------------------------------------')

split1 = couriers[0][2].split('[')
split2 = split1[1].split(']')

regions = [int(region) for region in split2[0].split(',')]

check_regions = []

for order in orders:
    if order[2] in regions:
        check_regions.append(order)


split3 = couriers[0][-1].split(',')[0].split('[')[-1].split('-')[0].split("'")[-1].split(':')
split4 = orders[0][-1].split(',')[0].split('[')[-1].split('-')[0].split("'")[-1].split(':')

wokrk_time = datetime(year=2021, month=3, day=25, hour=int(split3[0]), minute=int(split3[-1]))
delivery_time = datetime(year=2021, month=3, day=25, hour=int(split4[0]), minute=int(split4[-1]))

print(wokrk_time.time() <= delivery_time.time())

