from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import CreateJobRequest
from database import get_db
from models import Job


app = FastAPI()


@app.post("/")
def create(details: CreateJobRequest, db: Session = Depends(get_db)):
    to_create = Job(
        title=details.title,
        description=details.description
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }


@app.get('/list')
async def list_all(db: Session = Depends(get_db)):
    return db.query(Job).all()


@app.get("/")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.id == id).first()


@app.delete("/")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(Job).filter(Job.id == id).delete()
    db.commit()
    return {"success": True}


@app.get('/get')
async def get():
    return {
        'ok': 'ok'
    }
