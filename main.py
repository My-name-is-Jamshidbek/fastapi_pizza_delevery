from fastapi import FastAPI
from auth_r import auth_r
from order_r import ord_r
from fastapi_jwt_auth import AuthJWT
from schemas import Settings

app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_r)
app.include_router(ord_r)

