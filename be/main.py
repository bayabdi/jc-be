from fastapi import FastAPI
from db import models
from fastapi.middleware.cors import CORSMiddleware
from db.base import engine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from endpoints import job, user
app.include_router(job.router, prefix="/job", tags=["job"])
app.include_router(user.router, prefix="/user", tags=["user"])


@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind = engine)
