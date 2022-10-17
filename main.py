from fastapi import FastAPI
from auth_r import auth_r
from order_r import ord_r
app = FastAPI()
app.include_router(auth_r)
app.include_router(ord_r)

