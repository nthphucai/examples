import os

from fastapi import APIRouter
from dotenv import load_dotenv
from routes import generate, search

load_dotenv()

router = APIRouter()

router.include_router(search.router, tags=["Search"])
router.include_router(generate.router, tags=["Generate"])
