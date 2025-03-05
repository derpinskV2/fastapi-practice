from typing import Any

from fastapi import APIRouter

router = APIRouter(prefix="/test", tags=["Test"])

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Category One"},
    {"title": "Title Two", "author": "Author Two", "category": "Category Two"},
    {"title": "Title Three", "author": "Author Three", "category": "Category Three"},
    {"title": "Title Four", "author": "Author Four", "category": "Category Four"},
]


@router.get("/")
async def test() -> list[dict[str, Any]]:
    return BOOKS
