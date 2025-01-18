from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.api import api_router
from app.core.database import init_db
from loguru import logger

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="""
    Books API with Authentication and CRUD Operations.
    
    ## Features
    * 📚 Full CRUD operations for books
    * 🔐 JWT Authentication
    * 📄 Pagination support
    * 📡 Real-time updates with SSE
    
    ## Authentication
    1. Create user using `/api/v1/register`
    2. Get token using `/api/v1/token`
    3. Use token in Authorize button
    """,
    version="1.0.0"
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Books API")
    init_db()

@app.get("/")
async def root():
    return {
        "message": "Welcome to Books API",
        "documentation": "/docs"
    }
