from fastapi import APIRouter
from .endpoints import auth, books

api_router = APIRouter()

# Include authentication endpoints without prefix
api_router.include_router(auth.router, tags=["authentication"])

# Include books endpoints (prefix is already defined in books router)
api_router.include_router(books.router)