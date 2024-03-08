from fastapi import FastAPI
from user.UserController import router as users_router
from config.db_config import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users_router)
