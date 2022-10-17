from fastapi import APIRouter

auth_r = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@auth_r.get('/')
async def main1():
    return {'message':'Hello'}