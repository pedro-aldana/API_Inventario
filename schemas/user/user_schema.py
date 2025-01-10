from pydantic import BaseModel,EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    


class UserOut(BaseModel):
    id: int
    email: str
    subscription_status: bool
    created_at: datetime
    
    class Config:
        orm_mode = True
            
            

class Token(BaseModel):
    access_token: str
    token_type: str