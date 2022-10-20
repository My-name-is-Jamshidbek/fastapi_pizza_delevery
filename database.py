from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URI = "sqlite:///pizza_delivery.db"

Base = declarative_base()

engine = create_engine(  # 2
    SQLALCHEMY_DATABASE_URI,
    # required for sqlite
    connect_args={"check_same_thread": False},
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)