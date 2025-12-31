from peewee import Model
from app.db.session import db

class BaseModel(Model):
    class Meta:
        database = db
