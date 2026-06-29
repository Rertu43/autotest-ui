from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    """Модель базового юзера"""
    email: str = Field(..., description="Email-адрес пользователя")
    username: str = Field(..., description="Username пользователя")
    password: str = Field(..., description="Пароль пользователя")