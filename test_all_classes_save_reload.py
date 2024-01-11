#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Agege"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new Place --")
place = Place()
place.name = "Willy's hub"
place.description = "Good comfort place"
place.number_rooms = 5
place.number_bathrooms = 10
place.max_guest = 50
place.price_by_night = 500
place.lattitude = 120
place.longitude = 220
place.save()
print(place)

print("-- Create a new Amenity --")
amenity = Amenity()
amenity.name = "Swimming pool"
amenity.save()
print(amenity)

print("-- Create a new City --")
city = City()
city.name = "Vatican city"
city.save()
print(city)

print("-- Create a new State --")
state = State()
state.name = "Lagos"
state.save()
print(state)

print("-- Create a new Review --")
review = Review()
review.text = "This is a lovely app"
review.save()
print(review)
