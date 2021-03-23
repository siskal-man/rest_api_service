from fastapi import FastAPI, status, exceptions
from fastapi.responses import JSONResponse

from models.models import *

from db import insert_data_courier, update_data_courier, insert_data_order

app = FastAPI()


# couriers

@app.post('/couriers')
async def post_query_courier(data: СouriersPost):
    created_couriers = []
    error_id = []
    # сохранение курьера в системе
    for item in data.data:
        try:
            courier = {}
            courier[item['courier_id']] = {
                'courier_type': item['courier_type'],
                'regions': item['regions'],
                'working_hours': item['working_hours']
            }
            created_couriers.append({'id': item['courier_id']})
        except KeyError:
            error_id.append({'id': item['courier_id']})

    if error_id:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"validation_error": {"couriers": error_id}})
    else:
        for item in data.data:
            insert_data_courier(
                [item['courier_id'], item['courier_type'], str(item['regions']), str(item['working_hours'])])
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"couriers": created_couriers})


@app.patch('/couriers/{courier_id}')
async def patch_query_courier(courier_id: int, data: СouriersPatch):
    update_data_courier(courier_id, data.data)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"couriers": data.data})


###############################################################################

# orders

@app.post('/orders', response_model=OrdersPost)
async def post_query_order(data: OrdersPost):
    created_orders = []
    error_id = []
    # сохранение курьера в системе
    for item in data.data:
        try:
            order = {}
            order[item['order_id']] = {
                'weight': item['weight'],
                'region': item['region'],
                'delivery_hours': item['delivery_hours']
            }
            created_orders.append({'id': item['order_id']})
        except KeyError:
            error_id.append({'id': item['order_id']})

    if error_id:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"validation_error": {"orders": error_id}})
    else:
        insert_data_order([item['order_id'], item['weight'], str(item['region']), str(item['delivery_hours'])])
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"orders": created_orders})

@app.post('/orders/assign', response_model=OrdersAssignPost)
async def post_query_order_assign(data: OrdersAssignPost):
    pass

#
#
# @app.get('/couriers/get')
# async def get_query():
#     return couriers
#
#
# @app.get('/orders/get')
# async def get_query():
#     return orders
#
