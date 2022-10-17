from fastapi import APIRouter

ord_r = APIRouter(
    prefix='/order',
    tags=['Order']
)

@ord_r.get('/')
async def main1():
    return {'message':'Hello'}