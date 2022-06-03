#1/usr/bin/python
class vehicle:
    def __init__(self,max_speed,mileage_distance) :
        self.max_speed=max_speed
        self.mileage_distance=mileage_distance

    def maxSpeed(self):
        print("Vehicle Max Speed is ",self.max_speed, "Kph", "Mileage distance is ",self.mileage_distance, "Miles")

Toyota= vehicle(200,49900)
Toyota.maxSpeed() 

Volkswagen= vehicle(220,30900)
Volkswagen.maxSpeed()