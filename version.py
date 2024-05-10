import os

from dotenv import load_dotenv
from fastapi import APIRouter

from controllers import home, certs

load_dotenv()
prefixVersion = os.getenv("PREFIX_VERSION")

router = APIRouter( prefix = prefixVersion )

router.include_router(home.router)
router.include_router(certs.router)