from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.core.database import Base, engine
from app.routers.atleta import router as atleta_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Workout API - DIO")

app.include_router(atleta_router)
add_pagination(app)
