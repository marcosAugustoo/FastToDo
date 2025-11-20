from pydantic import BaseModel, EmailStr, Field


# criando schema userauth. qnd tiver cadastrando o usuario quero que passe email, username e password

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="Email do usuário")
    username: str = Field(..., min_length=5, max_length=50, description='nome do usuário')
    password: str = Field(..., min_length=5, max_length=15, description='senha do usuario')
