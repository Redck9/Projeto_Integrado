class Clock(object):
    
    def __init__(self, hour, minute):   
        self.minute = minute % 60 
        self.hour = (hour + (minute // 60)) % 24
    
    def __repr__(self):
        str_hour = f"{self.hour:02d}"
        str_minute = f"{self.minute:02d}"
        return str_hour + ":" + str_minute


    
    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        else:
            return False
        
    
    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    
    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
