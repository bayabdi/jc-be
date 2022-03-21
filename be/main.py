from fastapi import Depends, FastAPI
import uvicorn
from db import models
from db.base import engine

app = FastAPI()

from endpoints import job, user
app.include_router(job.router, prefix="/job", tags=["job"])
app.include_router(user.router, prefix="/user", tags=["user"])


@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind = engine)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
