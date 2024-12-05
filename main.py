from routes.user import users_router
from routes.login import login_router
from routes.course import course_router
from routes.opinion import opinion_router
from routes.registered import register_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import Base, engine
from fastapi.staticfiles import StaticFiles

app = FastAPI(docs_url="/")

app.mount("/images", StaticFiles(directory="images"), name="images")

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(login_router)
app.include_router(course_router)
app.include_router(opinion_router)
app.include_router(register_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)