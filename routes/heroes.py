from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database import SessionLocal
import schemas
import crud

router = APIRouter(
    prefix="/heroes"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.HeroModel])
def get_heroes(db: Session = Depends(get_db)):
    # create a get crud operation to return the list of Heroes
    # example: db.query(models.User).offset(skip).limit(limit).all()
    heroes = crud.get_heroes(db)
    return heroes

