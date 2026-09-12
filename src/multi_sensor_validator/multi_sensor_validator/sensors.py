import random

class Sensor:
    def __init__(self, min_range: int =10, max_range: int =200):
        if min_range > max_range:
            raise ValueError("min_range cannot be greater than max_range")
        self.min_range = min_range
        self.max_range = max_range
    def read_distance(self):
        return random.uniform(self.min_range, self.max_range)  # Simulate distance measurement in meters
   
   
class ultrasonic_sensor(Sensor):
    def __init__(self, sensor_id, min_range: int =10, max_range: int =200):
        super().__init__(min_range, max_range)



class Infrared_sensor(Sensor):
    def __init__(self, sensor_id, min_range: int =10, max_range: int =200):
        super().__init__(min_range, max_range)    