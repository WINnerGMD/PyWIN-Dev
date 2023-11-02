from fastapi import APIRouter
from src.auth.register import *
router = APIRouter(prefix='/auth',tags=['Auth'])

router.add_api_route(
    "/register",
    register,
    methods=['POST']
)


