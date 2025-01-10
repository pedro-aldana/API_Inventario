from tortoise import fields, Model
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model_stock import Stock

class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    price = fields.FloatField()

    category= fields.ForeignKeyField(
        "models.Category", related_name="products"
    )

    user = fields.ForeignKeyField(
        "models.User", related_name="products"
    )
    
    stock = fields.ReverseRelation["Stock"]

    def __repr__(self):
        return f"<Product id={self.id} name={self.name}>"