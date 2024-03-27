from pydantic import BaseModel

class Travel(BaseModel):
    travel_id: str
    name: str
    place_visited: str
    dates: str 
    budget: str 
    experience: str 
    suggestions: str 

class BucketList(BaseModel):
    bucket_id: str
    name: str
    destination: str
    dates: str 
    budget: str 
    experience: str 
    suggestions: str 
    
class PopularDestination(BaseModel):
    place_id: str
    place: str
    description: str 
