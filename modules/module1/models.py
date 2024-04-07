from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import Base, engine
from typing import List, Optional

class Dress(Base):
    __tablename__ = 'dresses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True, )
    color = Column(String(20), index=True)
    size = Column(Integer)

Base.metadata.create_all(engine)

def get_dress_by_id(db: Session, dress_id: int) -> Optional[Dress]:
    return db.query(Dress).filter(Dress.id == dress_id).first()

def get_dresses(db: Session, skip: int = 0, limit: int = 10) -> List[Dress]:
    return db.query(Dress).offset(skip).limit(limit).all()

def create_dress(db: Session, name: str, color: str, size: int) -> Dress:
    new_dress = Dress(name=name, color=color, size=size)
    db.add(new_dress)
    db.commit()
    db.refresh(new_dress)
    return new_dress

def update_dress(db: Session, dress_id: int, name: str, color: str, size: int) -> Optional[Dress]:
    dress = get_dress_by_id(db, dress_id)
    if dress:
        dress.name = name
        dress.color = color
        dress.size = size
        db.commit()
    return dress

def delete_dress(db: Session, dress_id: int) -> Optional[Dress]:
    dress = get_dress_by_id(db, dress_id)
    if dress:
        db.delete(dress)
        db.commit()
    return dress
