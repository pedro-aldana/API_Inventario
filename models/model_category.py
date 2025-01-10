# models/category/model_category.py
from tortoise import Model, fields

class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True, null=False)
    
    user = fields.ForeignKeyField(
        "models.User", related_name="categories"
    )

    

    def __repr__(self):
        return f"<Category id={self.id} name={self.name}>"
