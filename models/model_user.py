# models/user/model_user.py
from tortoise import Model, fields
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model_category import Category
    from model_product import Product

class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True, null=False)
    password = fields.CharField(max_length=255, null=False)
    role = fields.CharField(max_length=50, default="basic")
    subscription_status = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    
    products: fields.ReverseRelation["Product"]
    categories: fields.ReverseRelation["Category"]
    

    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"
