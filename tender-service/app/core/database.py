from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.federal_law import FederalLaw
from app.models.purchase_stage import PurchaseStage
from app.models.tender import Tender
from app.core.config import mongo_url


async def init_mongo_db():
    # Create Motor client
    client = AsyncIOMotorClient(
        mongo_url()
    )

    # Initialize beanie with a database
    await init_beanie(database=client.db_name, document_models=[FederalLaw, PurchaseStage, Tender])