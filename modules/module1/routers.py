from fastapi import APIRouter
from .views import get_dress

router = APIRouter()

router.get("/dress/{dress_id}")(get_dress)