from fastapi import FastAPI
from contextlib import asynccontextmanager
import fastapi_problem_details as pd
from app.config.database import create_tables, delete_tables
from app.routers.question_router import router as question_router
from app.routers.answer_router import router as answer_router


from app.config.logging_config import logger


logger.info("Starting the FastAPI application")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение приложения")


app = FastAPI(lifespan=lifespan)
pd.init_app(app, include_exc_info_in_response=True)

logger.info("Including routers: question_router, answer_router")
app.include_router(question_router)
app.include_router(answer_router)

logger.info("FastAPI application started successfully")
