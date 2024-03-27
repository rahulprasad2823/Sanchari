from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Travel
from model import BucketList
from model import PopularDestination 
#App object
app = FastAPI()

from database import (
    fetch_one_travel,
    fetch_all_travel,
    create_travel,
    update_travel,
    remove_travel,
    fetch_one_bucketlist,
    fetch_all_bucketlist,
    create_bucketlist,
    update_bucketlist,
    remove_bucketlist,
    fetch_one_popular_destination,
    fetch_all_popular_destinations,
    create_popular_destination,
    update_popular_destination,
    remove_popular_destination
)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Ping":"Pong"}

# Travel Experiences

@app.get("/api/travel")
async def get_travel():
    response = await fetch_all_travel()
    return response


@app.get("/api/travel{travel_id}", response_model=Travel)
async def get_travel_by_id(travel_id):
   response = await fetch_one_travel(travel_id)
   if response: 
        return response
   raise HTTPException(404, f"There is no Travel with this title {travel_id}")
   

@app.post("/api/travel", response_model=Travel)
async def post_travel(travel:Travel):
    response = await create_travel(travel.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")

@app.put("/api/travel{travel_id}", response_model=Travel)
async def put_travel(travel_id: str, name: str, place_visited: str, dates: str , budget: str, experience: str, suggestions: str ):
    response = await update_travel(travel_id, name, place_visited, dates, budget, experience, suggestions)
    if response:
        return response
    raise HTTPException(404, f"There is no Travel with this title {travel_id}")

@app.delete("/api/travel{travel_id}")
async def delete_travel(travel_id):
    response = await remove_travel(travel_id)
    if response:
        return "Sucesfully deleted trvael item !"
    raise HTTPException(404, f"There is no Travel with this title {travel_id}")



#Travel Bucketlist 

@app.get("/api/bucketlist")
async def get_bucketlist():
    response = await fetch_all_bucketlist()
    return response 

@app.get("/api/bucketlist/{bucket_id}", response_model=BucketList)
async def get_bucketlist_by_id(bucket_id: str):
    response = await fetch_one_bucketlist(bucket_id)
    if response:
        return response
    raise HTTPException(404, f"There is no BucketList item with this ID: {bucket_id}")

@app.post("/api/bucketlist", response_model=BucketList)
async def post_bucketlist(bucketlist: BucketList):
    response = await create_bucketlist(bucketlist.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")

@app.put("/api/bucketlist/{bucket_id}", response_model=BucketList)
async def put_bucketlist(bucket_id: str, name: str, destination: str, dates: str, plan: str):
    response = await update_bucketlist(bucket_id, name, destination, dates, plan)
    if response:
        return response
    raise HTTPException(404, f"There is no BucketList item with this ID: {bucket_id}")

@app.delete("/api/bucketlist/{bucket_id}")
async def delete_bucketlist(bucket_id: str):
    response = await remove_bucketlist(bucket_id)
    if response:
        return "Successfully deleted BucketList item!"
    raise HTTPException(404, f"There is no BucketList item with this ID: {bucket_id}")

#PopularDestination

@app.get("/api/popular_destination")
async def get_popular_destinations():
    response = await fetch_all_popular_destinations()
    return response 

@app.get("/api/popular_destination/{place_id}", response_model=PopularDestination)
async def get_popular_destination_by_id(place_id: str):
    response = await fetch_one_popular_destination(place_id)
    if response:
        return response
    raise HTTPException(404, f"There is no PopularDestination item with this ID: {place_id}")

@app.post("/api/popular_destination", response_model=PopularDestination)
async def post_popular_destination(popular_destination: PopularDestination):
    response = await create_popular_destination(popular_destination.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")

@app.put("/api/popular_destination/{place_id}", response_model=PopularDestination)
async def put_popular_destination(place_id: str, place: str, description: str):
    response = await update_popular_destination(place_id, place, description)
    if response:
        return response
    raise HTTPException(404, f"There is no PopularDestination item with this ID: {place_id}")

@app.delete("/api/popular_destination/{place_id}")
async def delete_popular_destination(place_id: str):
    response = await remove_popular_destination(place_id)
    if response:
        return "Successfully deleted PopularDestination item!"
    raise HTTPException(404, f"There is no PopularDestination item with this ID: {place_id}")
