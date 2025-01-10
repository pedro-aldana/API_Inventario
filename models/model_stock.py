from tortoise import fields, Model


class Stock(Model):
    id = fields.IntField(pk=True)
    quantity = fields.IntField()
    minimum_quantity = fields.IntField()
    
    
    product = fields.ForeignKeyField(
        "models.Product", related_name="stock"
    )
    
    def __repr__(self):
        return f"<Stock id={self.id} quantity={self.quantity} minimum_quantity={self.minimum_quantity}>"