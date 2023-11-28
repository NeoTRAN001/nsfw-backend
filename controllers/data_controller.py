from datetime import datetime
from fastapi import APIRouter, status, Body, HTTPException, Query
from fastapi.encoders import jsonable_encoder

from config.database import Session
from fastapi.responses import JSONResponse

from schemas.nsfw_schema import NsfwSchema
from services.nsfw_service import NSFWService

router = APIRouter()


@router.get(
    "/data/get",
    tags=['data'],
    response_model=NsfwSchema,
    summary='',
    description=''
)
def search_data(
    search: str = Query(None, description="Search text"),
    page: int = Query(1, gt=0, description="Page number"),
    limit: int = Query(20, gt=0, le=100, description="Number of results per page"),
):
    data = NSFWService(Session()).get_all(search, page, limit)

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(data))
