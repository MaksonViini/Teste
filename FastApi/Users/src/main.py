from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import CreateUsersRequest
from database import get_db
from models import Users

app = FastAPI()


@app.post('/')
async def create(details: CreateUsersRequest, db: Session = Depends(get_db)):
    to_create = Users(
        name=details.name,
        age=details.age,
        sex=details.sex
    )

    db.add(to_create)
    db.commit()

    return {
        'sucess': True,
        'created_id': to_create.id
    }


@app.get('/all')
async def read(db: Session = Depends(get_db)):
    return db.query(Users).all()


@app.get('/{id}')
async def read_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Users).filter(Users.id == id).first()


@app.put('/{id}')
async def update(id: int, details: CreateUsersRequest, db: Session = Depends(get_db)):
    to_update = {
        Users.name: details.name,
        Users.age: details.age,
        Users.sex: details.sex
    }
    db.query(Users).filter(Users.id == id).update(
        to_update, synchronize_session=False)

    db.commit()

    return {'sucess': True}


@app.delete('/{id}')
async def delete(id: int, db: Session = Depends(get_db)):
    db.query().filter(Users.id == id).delete()
    db.commit()

    return {
        'sucess': True
    }
