from datetime import datetime
from fastapi import APIRouter, status, Body, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()


@router.get("/data/get")
async def search_data(
    search: str = Query(..., description="Search text"),
    page: int = Query(1, gt=0, description="Page number"),
    limit: int = Query(20, gt=0, le=100, description="Number of results per page"),
):
    pass