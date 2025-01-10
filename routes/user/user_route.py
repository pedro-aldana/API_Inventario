from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from models.model_user import User
from schemas.user.user_schema import UserOut, Token, UserCreate
from auth.auth import create_access_token, verify_password, get_password_hash, get_current_user
from starlette.status import HTTP_201_CREATED, HTTP_200_OK


user_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@user_router.post("/register", response_model=UserOut, status_code=HTTP_201_CREATED)
async def register(user: UserCreate):
    
    # veriifar si el usuario existe
    existing_user = await User.get_or_none(email=user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    
    # creamos el usuario
    db_user = User(
        email=user.email,
        password=get_password_hash(user.password),
    )
    
    await db_user.save()
    return db_user


@user_router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    
    # consultar el usuario por email
    user = await User.get_or_none(email=form_data.username)
    
    # verificacion de usuario y la contraseña
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # crear el token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type": "bearer"}


@user_router.get("/me", response_model=UserOut)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user



