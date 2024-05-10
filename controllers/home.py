import datetime

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def index():
    return JSONResponse({
        'Status': 'ok',
        'Name'  : 'Danm API Profile',
        'Date'  : datetime.datetime.now().isoformat()
    })