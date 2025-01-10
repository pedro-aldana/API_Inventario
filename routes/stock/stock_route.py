from fastapi import APIRouter, HTTPException, Depends
from models.model_stock import Stock
from schemas.stock.stock_schema import StockCreate,StockOut,StockUpdate
from auth.auth import get_current_user
from models.model_user import User
from models.model_product import Product
from tortoise.transactions import in_transaction


stock_router = APIRouter()



# crear un stock
@stock_router.post("/create", response_model=StockOut)
async def create_stock(
    stock: StockCreate, user: User = Depends(get_current_user)
):
    async with in_transaction() as conn:
        stock_obj = await Stock.create(quantity=stock.quantity, minimum_quantity=stock.minimum_quantity, product_id=stock.product_id)
    
    # Asegúrate de que el objeto product esté cargado
    stock_obj = await Stock.filter(id=stock_obj.id).prefetch_related("product").first()

    return stock_obj  



# obtener lista de stocks
@stock_router.get("/list", response_model=list[StockOut])
async def get_stocks(user: User = Depends(get_current_user)):
    stocks = await Stock.filter(product__user_id=user.id).prefetch_related("product")
    return stocks



# obtener un stock por ID
@stock_router.get("/by_id/{stock_id}", response_model=StockOut)
async def get_stock(stock_id: int, user: User = Depends(get_current_user)):
    stock = await Stock.filter(id=stock_id).prefetch_related("product").first()
    if not stock or stock.product.user_id != user.id:
        raise HTTPException(status_code=404, detail="Stock no encontrado o no autorizado")
    return stock


# actualizar un stock

@stock_router.put("/update/{stock_id}", response_model=StockOut)
async def update_stock(
    stock_id: int, 
    stock: StockUpdate, 
    user: User = Depends(get_current_user)
):
    # Buscar el stock y verificar que pertenece a un producto del usuario
    stock_obj = await Stock.filter(id=stock_id).prefetch_related("product").first()

    if not stock_obj or stock_obj.product.user_id != user.id:
        raise HTTPException(status_code=404, detail="Stock no encontrado o no autorizado")

    # Actualizar los campos del stock
    stock_obj.quantity = stock.quantity
    stock_obj.minimum_quantity = stock.minimum_quantity

    # Solo actualiza product_id si es diferente del actual
    if stock.product_id and stock.product_id != stock_obj.product_id:
        stock_obj.product_id = stock.product_id

    # Guardar los cambios
    await stock_obj.save()

    return stock_obj



# eliminar un stock
@stock_router.delete("/delete/{stock_id}")
async def delete_stock(
    stock_id: int,
    user: User = Depends(get_current_user)
):
    stock_obj = await Stock.filter(id=stock_id).prefetch_related("product").first()
    
    
    # verificar si el stock existe y si el usuario tiene acceso al producto relacionado
    
    if not stock_obj or stock_obj.product.user_id != user.id:
        raise HTTPException(status_code=404, detail="Stock no encontrado o no autorizado")
    
    
    # eliminar el stock de la bd
    await stock_obj.delete()
    
    return {"message": "Stock eliminado correctamente"}