from pydantic import BaseModel, Field

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer"
            }
        }

class TokenData(BaseModel):
    username: str | None = None

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "testuser",
                "password": "testpass123"
            }
        }

class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        from_attributes = True