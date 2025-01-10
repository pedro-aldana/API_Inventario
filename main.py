from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from db.db import init,close
from tortoise.contrib.fastapi import register_tortoise
from auth.auth import verify_token
from routes.user.user_route import user_router
from routes.category.category_route import category_router
from routes.product.product_route import product_router
from routes.stock.stock_route import stock_router

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost"
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir solo estos orígenes
    allow_credentials=True, # Permitir enviar cookies y credenciales
    allow_methods=["*"],    # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],    # Permitir todos los headers
)


@app.post("/verify-token")
def verify_token_route(token: str = Depends(oauth2_scheme)):
    # Verifica el token
    verify_token(token)
    return {"message": "Token válido"}

@app.on_event("startup")
async def startup_event():
    await init()

@app.on_event("shutdown")
async def shutdown_event():
    await close()


register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={
            'models': [
                'models.model_user',
                'models.model_category',
                'models.model_product',
            ]
    },
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(user_router, prefix="/api/users")
app.include_router(category_router, prefix="/api/category")
app.include_router(product_router, prefix="/api/product")
app.include_router(stock_router, prefix="/api/stock")