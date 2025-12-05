from app.user.user_repository import user_repository
from app.user.user_schema import UserInDb

import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_MEMORY_URL, connect_args={"check_same_thread": False})
local_session = sessionmaker(autoflush=False, bind=engine)


@pytest.fixture
async def test_create_user():
    with local_session() as db:
        user = UserInDb(
            first_name="gustavo",
            last_name="silva",
            email="test@gmail.com",
            password="Senha123"
        )
        user_response = await user_repository.add_user(db, user)

        assert user_response.id == 1
        assert user_response.first_name == user.first_name
        assert user_response.last_name == user.last_name
        assert user_response.email == user.last_name
