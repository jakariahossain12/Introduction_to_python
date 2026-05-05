from ride import Ride,RideMatching,RideRequest,RideSharing
from users import Rider,Driver
from vehicle import Car,Bike

j = RideSharing("niye jan")

rahim = Rider('rahim','rihim@gmail.com',12342,'mohakhali',1200)

j.add_rider(rahim)

jaka = Driver('jakria','jakaria@gmail.com',14323,'gulshan')

j.add_driver(jaka)

rahim.request_ride(j,'uttara','car')

rahim.show_current_ride()

jaka.reach_destination(rahim.current_ride)

print(j)