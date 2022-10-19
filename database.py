from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine = create_engine("postgresql://postgres:postgres@db:5432/pizza_delivery",
                       echo = True)
Base = declarative_base()
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
