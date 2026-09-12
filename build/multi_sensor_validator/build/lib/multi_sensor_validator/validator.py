class Validator:
    CONSISTENT_MSG = "Sensor readings consistent"
    INCONSISTENT_MSG = "Sensor readings inconsistent"
    
    def __init__(self, threshold: int = 20):
        self.threshold = threshold
        
    def validate(self, ultrasonic_value, infrared_value):    
        if ultrasonic_value is None or infrared_value is None:
            return None
         
        difference = abs(ultrasonic_value - infrared_value)
        if difference <= self.threshold: 
          return self.CONSISTENT_MSG
        return self.INCONSISTENT_MSG
        