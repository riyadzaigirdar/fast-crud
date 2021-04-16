from fastapi import FastAPI
from model import model
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

# model.Car_dant.from_queryset(model.Car.all())
# model.Car.filter(id=2)
# model.CarIn_dant.from_queryset_single(model.Car.get(id=id))
# model.Car.get(id=id)


@app.get("/car")
async def list():
    # model.Car.filter(id=2)
    objs = await model.Car_dant.from_queryset(model.Car.all())
    return objs


@app.post("/car/")
async def create(data: model.CarIn_dant):
    obj = await model.Car.create(**data.dict(exclude_unset=True))
    return await model.CarIn_dant.from_tortoise_orm(obj)


@app.get("/car/{id}")
async def get_detail(id: int):
    obj = await model.Car_dant.from_queryset_single(model.Car.get(id=id))
    return obj


@app.patch("/car/{id}")
async def update(id: int, data: model.CarIn_dant):
    await model.Car.filter(id=id).update(**data.dict(exclude_unset=True))
    return await model.Car_dant.from_queryset_single(model.Car.get(id=id))

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["model.model"]},
    generate_schemas=False,
    add_exception_handlers=True
)
