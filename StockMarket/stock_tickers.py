import random
random.seed()

class Ticker:
    def __init__(self):
        self.name = "Stock"
        self.short_name = "STK"
        self.desc = "A company that does not exitst."
        self.values = []
        self.current_value = 100
        self.last_value = 100
        self.products = []
        
        self.performance = 0
        self.fluctuational_coefficient = 1
        self.average_optimism = 0
        self.current_trend = 0
        self.last_trend = 0
        self.speculation = 0
        self.bankrupt = False
        
        self.disp_value_change = 0
        self.optimism = 0
        self.last_unification = 0
        self.average_shares = 100
        
        self.outside_shareholders = 10000
        self.available_shares = 500000
        
        self.borrow_brokers = []
        self.shareholders = []
        self.borrows = []
        self.events = []
        self.articles = []
        self.fluctuation_rate = 15
        self.fluctuation_counter = 0
        self.industry = None
        
    def addEvent(self, E):
        self.events = self.events | E
        
    def addArticle(self, A):
        if(A not in self.articles):
            self.articles.insert(0,A)
            
    def genereateEvents(self):
        # TODO
        pass
    
    def generateEvent(self,type):
        # TODO
        E = None
        self.addEvent(E)
        
    def affectPublicOpinion(self, boost):
        self.optimism += random.randint(0, 500) / 500 * boost
        self.average_optimism += random.randint(0,150) / 5000 * boost
        self.speculation += random.randint(-5, 25) / 10 * boost
        self.performance += random.randint(0, 110) / 100 * boost
        
    def generateIndustry(self):
        # TODO
        if self.name.find("Farms"):
            self.industry = None
        elif any(x in self.name for x in ["Software","Programming","IT Group","Electronics","Electric","Nanotechnology"]):
            self.industry = None
        elif self.name.find("Mobile") | self.name.find("Communications"):
            self.industry = None
        elif self.name.find("Pharmaceuticals") | self.name.find("Health"):
            self.industry = None
        elif self.name.find("Wholesale") | self.name.find("Stores"):
            self.industry = None
        else:
            pass