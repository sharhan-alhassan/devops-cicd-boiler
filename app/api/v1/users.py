from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any
from app.core.security import create_access_token
from app.crud.users import user_crud
from app.db.session import get_async_session
from app.schemas.user import (
    User,
    UserCreate,
    GenericDetailResponse,
    LoginResponse,
)
from fastapi.security import OAuth2PasswordRequestForm
from app.core.deps import get_current_user
from app.config import settings
from datetime import timedelta


class UserRouter:
    def __init__(self):
        self.router = APIRouter()
        self.prefix = "/users"
        self.tags = ["users"]
        self.singular = "user"
        self.plural = "users"

        self.router.add_api_route(
            "/register",
            self.register,
            methods=["POST"],
            response_model=GenericDetailResponse,
            status_code=status.HTTP_201_CREATED,
            summary="Register new user",
        )

        self.router.add_api_route(
            "/login",
            self.login,
            methods=["POST"],
            summary="User login",
            status_code=status.HTTP_200_OK,
            response_model=LoginResponse,
            description="""
            
            """,
        )

        self.router.add_api_route(
            "/me",
            self.get_me,
            methods=["GET"],
            response_model=User,
            summary="Get current user",
        )

    async def register(
        self, user_in: UserCreate, db: AsyncSession = Depends(get_async_session)
    ) -> Any:
        if user_in.password != user_in.confirm_password:
            raise HTTPException(status_code=400, detail="Passwords do not match")
        user = await user_crud.get_by_email(db, email=user_in.email)
        if user:
            raise HTTPException(
                status_code=400,
                detail="A user with this email already exists! If this is your account, request an OTP to activate your account",
            )

        user = await user_crud.create(db, obj_in=user_in)

        return {"detail": f"Registration successful for {user.email}"}

    async def login(
        self,
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: AsyncSession = Depends(get_async_session),
    ) -> Any:
        existing_user = await user_crud.get_by_email(db, email=form_data.username)
        if not existing_user:
            raise HTTPException(detail="User does not exists", status_code=400)
        user = await user_crud.authenticate(
            db,
            email=form_data.username.lower(),
            password=form_data.password,
        )
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")

        if not user.is_active:
            user.is_active = True
            await user_crud.update(db, db_obj=user, obj_in={"is_active": True})

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(user.id, access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}

    async def get_me(
        self,
        current_user: User = Depends(get_current_user),
    ) -> Any:
        return current_user


user_router = UserRouter()
