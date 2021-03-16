from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel
from typing import List, Optional, Dict



app = FastAPI()

#couriers
couriers = {}

class Сouriers_post(BaseModel):
    data: List = None


class Сouriers_patch(BaseModel):
    data: List = None


@app.post('/couriers', response_model=Сouriers_post)
async def post_query(data: Сouriers_post):
    created_couriers = []
    error_id = []
    # сохранение курьера в системе
    for item in data.data:
        try:
            couriers[item['courier_id']] = {
                'courier_type': item['courier_type'],
                'regions': item['regions'],
                'working_hours': item['working_hours']
            }

            created_couriers.append({'id': item['courier_id']})
        except Exception:
            error_id.append({'id': item['courier_id']})
    
    if error_id:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"validation_error": {"couriers": error_id}})
    else:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"couriers": created_couriers})

# TODO: не работает, нужно починить
# @app.patch('/couriers/{courier_id}', response_model=Сouriers_patch)
# async def patch_query(courier_id: int, data: Сouriers_patch):
#     stored_item_data = couriers[courier_id]
#     stored_item_model = Сouriers_patch(**stored_item_data)
#     update_data = data.dict(exclude_unset=True)
#     updated_item = stored_item_model.copy(update=update_data)
#     couriers[courier_id] = jsonable_encoder(updated_item)
#     return updated_item

###############################################################################

#orders

orders = {}

class Orders_post(BaseModel):
    data: List = None


@app.post('/orders', response_model=Orders_post)
async def post_query(data: Orders_post):
    created_orders = []
    error_id = []
    # сохранение курьера в системе
    for item in data.data:
        try:
            orders[item['order_id']] = {
                "weight": item["weight"],
                "region": item["region"],
                "delivery_hours": item["delivery_hours"]
            }

            created_orders.append({'id': item['order_id']})
        except Exception:
            error_id.append({'id': item['order_id']})
    
    if error_id:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"validation_error": {"orders": error_id}})
    else:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"orders": created_orders})



@app.get('/couriers/get')
async def get_query():
    return couriers


@app.get('/orders/get')
async def get_query():
    return orders

