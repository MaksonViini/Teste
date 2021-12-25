from typing import Optional
from odmantic import Field, Model, AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

uri = 'mongodb://root:example@localhost:27017/'

client = AsyncIOMotorClient(uri)
engine = AIOEngine(motor_client=client, database='Publisher')


class Publisher(Model):
    name: str
    founder: int = Field(int, required=True)
    location: Optional[str] = Field(str, required=True)


instances = [
    Publisher(name='Apress', founder=1955, location='USA'),
    Publisher(name='Packt', founder=2010, location='USA'),
    Publisher(name='O\'Reilly', founder=1981, location='USA'),
    Publisher(name='Wiley', founder=1955, location='USA'),
    Publisher(name='McGraw-Hill', founder=1955, location='USA'),
]

async def save() -> asyncio.coroutine:
    await engine.save_all(instances)



asyncio.run(save())
