from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

couriers = {}
orders = {}


class CouriersDataPost(BaseModel):
    courier_id: int
    courier_type: str
    regions: list
    working_hours: list


class CouriersDataPatch(BaseModel):
    courier_type: str
    regions: list
    working_hours: list


class OrderDataPost(BaseModel):
    order_id: int
    weight: float
    region: int
    delivery_hours: list


app = FastAPI()


@app.get('/get_couriers')
async def get_list():
    return couriers


# couriers api
@app.post("/couriers")
async def create_courier(data: dict):
    for item in data['data']:
        couriers[item['courier_id']] = [{
            'courier_type': item['courier_type'],
            'regions': item['regions'],
            'working_hours': item['working_hours']
        }]

    all_id = len(couriers)
    id_list = []
    for index in range(all_id):
        id_list.append({'id': index})
    return 'HTTP 201 Created', {"couriers": id_list}


# TODO: Не работает
@app.patch('/couriers/{courier_id}', response_model=CouriersDataPatch)
async def update_item(courier_id: str, data: CouriersDataPatch):
    stored_item_data = couriers[courier_id]

    stored_item_data[0].update({'courier_type': data.courier_type,
                                'regions': data.regions, 'working_hours': data.working_hours})


# orders api
@app.get('/get_orders')
async def get_list():
    return orders


@app.post("/orders")
async def create_courier(data: OrderDataPost):
    orders[data.order_id] = [{
        'weight': data.weight,
        'region': data.region,
        'delivery_hours': data.delivery_hours
    }]

    all_id = len(orders)
    id_list = []
    for index in range(all_id):
        id_list.append({'id': index})
    return 'HTTP 201 Created', {"orders": id_list}

