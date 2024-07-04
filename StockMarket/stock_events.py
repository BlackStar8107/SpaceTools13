import random
import math

class Event:
    def __init__(self):
        self.name = "event"
        self.next_phase = 0
        self.company = None
        self.current_title = "A company holding an pangalactic conference in the Seattle Conference Center, Seattle, Earth"
        self.current_desc = "We will continue to monitor their stocks as the situation unfolds."
        self.phase_id = 0
        self.hidden = False
        self.finished = 0
        self.last_change = 0
        
    def process(self):
        # TODO: Look at how this works!
        finished = True # Temp for errors!
        if finished:
            return
        else:
            self.transition()
    
    def transition(self):
        return
    
    def spacetime(self, ticks):
        seconds = math.floor(ticks / 10)
        minutes = math.floor(seconds / 60)
        seconds -= minutes * 60
        return f"{minutes}:{seconds}"
    
class Product:
    def __init__(self, S):
        self.name = "product"
        self.product_name = ""
        self.product_article = None
        self.effect = 0
        self.company = S
        self.mins = random.randint(5, 20)
        self.next_phase = self.mins * 600 # TODO: Write ticker fuckery
        self.current_title = "Product demo"
        self.current_desc = S.industry.detokenise(f"{S.name} will unveil a new product on an upcoming %industrial% conference held at spacetime {self.spacetime(self.next_phase)}")
        # TODO: Look at how this works
        # S.addEvent()