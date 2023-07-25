import motor.motor_asyncio
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

host = "cluster0.rusc6nw.mongodb.net"
username = "devilnut28"
password = "<password>"
database_name = "app_mobile"

# Créez la "Connection URI"
MONGODB_URI = f"mongodb+srv://{username}:{password}@{host}/{database_name}?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client[database_name]

async def get_db():
    db = client[database_name]
    try:
        yield db
    finally:
        await client.close()