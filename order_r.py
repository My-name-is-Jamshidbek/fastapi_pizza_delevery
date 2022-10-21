from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import User,Order
from schemas import OrderModel
from database import Session, engine
from fastapi.encoders import jsonable_encoder

ord_r = APIRouter(
    prefix='/order',
    tags=['Order']
)

session = Session(bind=engine
                  )
@ord_r.get('/')
async def hello(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Token'
        )
    return {'message':'Hello'}

@ord_r.get("/order",status_code=status.HTTP_201_CREATED)
async def place_an_order(order:OrderModel,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Token'
        )
    current_user = Authorize.get_jwt_subject()

    user = session.query(User).filter(User.username==current_user).first()

    new_order = Order(
        pizza_size=order.pizza_size,
        quantity=order.quantity
    )
    new_order.user=user
    session.add(new_order)
    session.commit()

    res = {
        "pizza_size":new_order.pizza_size,
        "quantity":new_order.quantity,
        "id":new_order.id,
        "order_status":new_order.ORDER_STATUS
    }

    return jsonable_encoder(res)

@ord_r.get('/orders')
async def list_all_ord(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid Token')
    current_user = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.username==current_user).first()

    if user.is_staff:
        orders=session.query(Order).all()
        return jsonable_encoder(orders)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='You are not a superuser')