import datetime

import uvicorn
from fastapi import FastAPI, HTTPException # Чтобы вернуть клиенту HTTP-ответы с ошибками
import database as db
import models
from typing import List   # можно типировать целые листы типа List[int]
from random import randint


app = FastAPI()  # создаем приложение


@app.get('/')   # создаем декоратор  получения стартовой страницы с выводом словаря
def root():
    return {'Message': "Final Task"}


@app.get('/fake_users/{count}')    # создание юзеров с добавлением в конце ко всем числа
async def create_users(count: int):# в асинхронной функции
    for i in range(count):
        query = db.users.insert().values(name=f'users{i}', surname=f'surname{i}',
                                         email=f'email{i}@yandex.ru', password=f'qwerty{i}')
        await db.database.execute(query)  # await. Он говорит интерпретатору примерно следующее: "я тут возможно немного потуплю, но ты меня не жди — пусть выполняется другой код, а когда у меня будет настроение продолжиться, я тебе маякну"
    return {'message': f'{count} fake users create'}  # execute функция базы данны для выполнения команды( т.е говорит выполни то, что сверху query


@app.get('fake_products/{count}')
async def create_products(count: int):
    for i in range(count):
        query = db.users.insert().values(title=f'product {i}', description=f'about product{i}', price=randint(1, 10000))
        await db.database.execute(query)
    return {'message': f'{count} fake products create'}


@app.get("/fake_orders/{count}")
async def create_orders(count: int):
    for i in range(count):
        query = db.orders.insert().values(user_id=randint(1, 20), prod_id=randint(1, 20), status="created",
                                          date=datetime.datetime.now())
        await db.database.execute(query)
    return {'message': f'{count} fake orders create'}


@app.get("/users/", response_model=List[models.UserRead]) # response_modelполучает тот же тип, который вы бы объявили для поля модели Pydantic, поэтому это может быть модель Pydantic, но также может быть, например, listмодель Pydantic, например List[Item]
async def read_users():
    query = db.users.select()
    return await db.database.fetch_all(query)


@app.get("/products/", response_model=List[models.ProductRead])
async def read_products():
    query = db.products.select()
    return await db.database.fetch_all(query)


@app.get("/orders/", response_model=List[models.OrderRead])
async def read_orders():
    query = db.orders.select()
    return await db.database.fetch_all(query)


# Чтение одного юзера, продукта и заказа

@app.get("/users/{user_id}", response_model=models.UserRead)
async def read_user(user_id: int):
    query = db.users.select().where(db.users.c.id == user_id) # ИЗ базы данных колонка c
    user = await db.database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found") # если такого персонажа нет,выкидываем ошибку, иначе возвращаем его
    return user


@app.get("/products/{product_id}", response_model=models.ProductRead)
async def read_product(product_id: int):
    query = db.products.select().where(db.products.c.id == product_id)
    product = await db.database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.get("/orders/{order_id}", response_model=models.OrderRead)
async def read_order(order_id: int):
    query = db.orders.select().where(db.orders.c.id == order_id)
    order = await db.database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# замена юзера, продукта и заказа по id

@app.put("/users/{user_id}", response_model=models.UserRead)
async def update_user(user_id: int, new_user: models.UserCreate):
    query = db.users.update().where(db.users.c.id == user_id).values(**new_user.dict())
    await db.database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.put("/products/{product_id}", response_model=models.ProductRead)
async def update_product(product_id: int, new_product: models.ProductCreate):
    query = db.products.update().where(db.products.c.id == product_id).values(**new_product.dict())
    await db.database.execute(query)
    return {**new_product.dict(), "id": product_id}


@app.put("/orders/{order_id}", response_model=models.OrderRead)
async def update_order(order_id: int, new_order: models.OrderCreate):
    query = db.orders.update().where(db.orders.c.id == order_id).values(**new_order.dict())
    await db.database.execute(query)
    return {**new_order.dict(), "id": order_id}


# удаление

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = db.users.delete().where(db.users.c.id == user_id)
    await db.database.execute(query)
    return {'message': 'User deleted'}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = db.products.delete().where(db.products.c.id == product_id)
    await db.database.execute(query)
    return {'message': 'Product deleted'}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = db.orders.delete().where(db.orders.c.id == order_id)
    await db.database.execute(query)
    return {'message': 'Order deleted'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)