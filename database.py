import motor.motor_asyncio
host = "cluster0.rusc6nw.mongodb.net"
port = 27017
username = "devilnut28"
password = "<password>"
database_name = "app_mobile"

# Create the "Connection URI"
MONGODB_URI = f"mongodb+srv://{username}:{password}@{host}:{port}/{database_name}?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client[database_name]
collection = db.collection("app_mobs")


async def get_db():
    db = await db.client().start_session()
    try:
        yield db
    finally:
        await db.close()