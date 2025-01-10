from pydantic import BaseModel
from typing import Optional
from schemas.product.product_schema import ProductOut


class StockCreate(BaseModel):
    quantity: int
    minimum_quantity: int
    product_id: int
    
    

class StockUpdate(BaseModel):
    quantity: Optional[int]
    minimum_quantity: Optional[int]
    product_id: Optional[int]
    
class StockOut(BaseModel):
    id: int
    quantity: int
    minimum_quantity: int
    product_id: int
    product: ProductOut
    
    class Config:
        orm_mode = True 
    