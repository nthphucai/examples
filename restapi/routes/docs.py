import fastapi
from fastapi.openapi.docs import get_swagger_ui_html


router = fastapi.APIRouter()


@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="QuizExpertAI API",
    )
