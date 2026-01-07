import uvicorn
from fastapi import FastAPI

from user import user_router
from auth import auth_router
from models.base import Base
from post import post_router
from db.session import engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(engine)

app = FastAPI(title="OnlyReads")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router.router)
app.include_router(auth_router.router)
app.include_router(post_router.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)