from fastapi import HTTPException
from database import SessionLocal
from modules.module1.models import get_dress_by_id

async def get_dress(dress_id: int):
    db = SessionLocal()
    try:
        dress = get_dress_by_id(db, dress_id)
        if dress is None:
            raise HTTPException(status_code=404, detail="Dress not found")
        return dress.__dict__
    finally:
        db.close()
