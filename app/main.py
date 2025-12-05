import uvicorn
from fastapi import FastAPI

from user import user_router
from auth import auth_router
from enterprise import enterprise_router
from models.base import Base

from db.session import engine

Base.metadata.create_all(engine)

app = FastAPI(title="Material search")

app.include_router(user_router.router)
app.include_router(auth_router.router)
app.include_router(enterprise_router.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)