from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    email: EmailStr
    phone_number: str = Field(..., min_length=10, max_length=15)


class SignupResponse(BaseModel):
    message: str