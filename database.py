from model import Travel
from model import BucketList
from model import PopularDestination

#MongoDb driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.Travel
collection = database.travelData


#Travel Experiences
async def fetch_one_travel(travel_id):
    document = await collection.find_one({"travel_id":travel_id})
    return document

async def fetch_all_travel():
    travels = []
    cursor = collection.find({})
    async for document in cursor:
        travels.append(Travel(**document))
    return travels  

async def create_travel(travel):
    document = travel 
    result = await collection.insert_one(document)
    return document

async def update_travel(travel_id, name, place_visited, dates, budget, experience, suggestions):
    await collection.update_one({"travel_id":travel_id},{"$set":{"name":name,"place_visited":place_visited,"dates":dates,"budget":budget,"experience":experience,"suggestions":suggestions}}) 
    document = await collection.find_one({"title":travel_id})
    return document

async def remove_travel(travel_id):
    await collection.delete_one({"travel_id":travel_id})
    return True

#Travel BucketList

bucketlist_collection = database.BucketList

async def fetch_one_bucketlist(bucket_id):
    document = await bucketlist_collection.find_one({"bucket_id": bucket_id})
    return document

async def fetch_all_bucketlist():
    bucketlist_items = []
    cursor = bucketlist_collection.find({})
    async for document in cursor:
        bucketlist_items.append(BucketList(**document))
    return bucketlist_items  

async def create_bucketlist(bucketlist_item):
    document = bucketlist_item 
    result = await bucketlist_collection.insert_one(document)
    return document

async def update_bucketlist(bucket_id, name, destination, dates, plan):
    await bucketlist_collection.update_one(
        {"bucket_id": bucket_id},
        {"$set": {"name": name, "destination": destination, "dates": dates, "plan": plan}}
    )
    document = await bucketlist_collection.find_one({"bucket_id": bucket_id})
    return document

async def remove_bucketlist(bucket_id):
    await bucketlist_collection.delete_one({"bucket_id": bucket_id})
    return True

#PopularDestination
popular_destination_collection = database.Popular

async def fetch_one_popular_destination(place_id):
    document = await popular_destination_collection.find_one({"place_id": place_id})
    return document

async def fetch_all_popular_destinations():
    popular_destinations = []
    cursor = popular_destination_collection.find({})
    async for document in cursor:
        popular_destinations.append(PopularDestination(**document))
    return popular_destinations  

async def create_popular_destination(popular_destination_item):
    document = popular_destination_item 
    result = await popular_destination_collection.insert_one(document)
    return document

async def update_popular_destination(place_id, place, description):
    await popular_destination_collection.update_one(
        {"place_id": place_id},
        {"$set": {"place": place, "description": description}}
    )
    document = await popular_destination_collection.find_one({"place_id": place_id})
    return document

async def remove_popular_destination(place_id):
    await popular_destination_collection.delete_one({"place_id": place_id})
    return True
