from peewee import MySQLDatabase
from app.core.config import settings

db = MySQLDatabase(
    settings.MYSQL_DB,
    user=settings.MYSQL_USER,
    password=settings.MYSQL_PASSWORD,
    host=settings.MYSQL_SERVER,
    port=settings.MYSQL_PORT,
    charset='utf8mb4'
)
