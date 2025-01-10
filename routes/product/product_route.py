from fastapi import APIRouter, HTTPException, Depends
from models.model_product import Product
from schemas.product.product_schema import ProductCreate,ProductOut,ProductUpdate
from auth.auth import get_current_user
from models.model_user import User
from tortoise.transactions import in_transaction


product_router = APIRouter()


# crear un producto
@product_router.post("/create", response_model=ProductOut)
async def create_product(
    product: ProductCreate, user: User = Depends(get_current_user)
):
    async with in_transaction() as conn:
        product_obj = await Product.create(name=product.name, description=product.description, price=product.price,category_id=product.category_id ,user_id=user.id)
        
    return product_obj    


# obtener lista de productos (requiere autenticacion)

@product_router.get("/list", response_model=list[ProductOut])
async def get_products(user: User = Depends(get_current_user)):
    return await Product.filter(user_id=user.id)


# obtener un producto por ID (require autenticacion)

@product_router.get("/by_id/{product_id}", response_model=ProductOut)
async def get_product(product_id: int, user: User = Depends(get_current_user)):
    product = await Product.get(id=product_id, user_id=user.id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

# actualizar un producto (require autenticacion )

@product_router.put("/update/{product_id}", response_model=ProductOut)
async def update_product(
    product_id: int,
    product: ProductUpdate, user: User = Depends(get_current_user)
):
    product_obj = await Product.get(id=product_id, user_id=user.id)
    if not product_obj:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    product_obj.name = product.name
    product_obj.description = product.description
    product_obj.price = product.price
    product_obj.category_id = product.category_id
    await product_obj.save()
    return product_obj



# eliminar un producto (require autenticacion)

@product_router.delete("/delete/{product_id}")
async def delete_product(product_id: int, user: User = Depends(get_current_user)):
    product = await Product.get(id=product_id, user_id=user.id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    await product.delete()
    return {"message": "Producto eliminado con exito"}

