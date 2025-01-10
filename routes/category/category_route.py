from fastapi import APIRouter, HTTPException, Depends
from models.model_category import Category
from schemas.category.category_schema import CategoryCreate, CategoryOut
from auth.auth import get_current_user  # Ya tienes esta función de autenticación
from models.model_user import User
from tortoise.transactions import in_transaction

category_router = APIRouter()

# Crear una categoría (requiere autenticación)
@category_router.post("/create", response_model=CategoryOut)
async def create_category(
    category: CategoryCreate,
    user: User = Depends(get_current_user)  
):
    async with in_transaction() as conn:
        category_obj = await Category.create(name=category.name, user_id=user.id)  # 
    return category_obj

# Obtener lista de categorías (requiere autenticación)
@category_router.get("/list", response_model=list[CategoryOut])
async def get_categories(user: User = Depends(get_current_user)):  
    return await Category.filter(user_id=user.id)  

# Obtener una categoría por ID (requiere autenticación)
@category_router.get("/by_id/{category_id}", response_model=CategoryOut)
async def get_category(category_id: int, user: User = Depends(get_current_user)):  
    category = await Category.get(id=category_id, user_id=user.id)  
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return category

# Actualizar una categoría (requiere autenticación)
@category_router.put("/update/{category_id}", response_model=CategoryOut)
async def update_category(
    category_id: int, 
    category: CategoryCreate,
    user: User = Depends(get_current_user)  
):
    category_obj = await Category.get(id=category_id, user_id=user.id)  
    if not category_obj:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    category_obj.name = category.name
    await category_obj.save()
    return category_obj

# Eliminar una categoría (requiere autenticación)
@category_router.delete("/delete/{category_id}")
async def delete_category(category_id: int, user: User = Depends(get_current_user)):  
    category = await Category.get(id=category_id, user_id=user.id) 
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    await category.delete()
    return {"message": "Categoría eliminada correctamente"}
