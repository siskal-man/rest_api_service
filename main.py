from fastapi import FastAPI, status, HTTPException
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
            insert_data_courier(
                [item['courier_id'], item['courier_type'], str(item['regions']), str(item['working_hours'])])
            created_couriers.append({'id': item['courier_id']})
        except Exception:
            error_id.append({'id': item['courier_id']})

    if error_id:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"validation_error": {"couriers": error_id}})
    else:
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
            insert_data_order([item['order_id'], item['weight'], str(item['region']), str(item['delivery_hours'])])
            created_orders.append({'id': item['order_id']})
        except Exception:
            error_id.append({'id': item['order_id']})

    if error_id:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"validation_error": {"orders": error_id}})
    else:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"orders": created_orders})

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
