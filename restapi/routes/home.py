import fastapi


router = fastapi.APIRouter()


@router.get("/", include_in_schema=False)
async def index():
    return "API is serving..."
