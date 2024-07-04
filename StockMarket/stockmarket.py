import random
import math
import stock_tickers

random.seed()

consonants_upper = ["A","E","I","O","U"]
consonants_lower = ["a","e","i","o","u"]
vowels_upper = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
vowels_lower = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

class Market():
    def __init__(self):
        self.stocks = []
        self.stockBrokers = []
        self.balances = []
        self.last_read = []
        
        self.generateBrokers()
        self.generateStocks()
    
    def generateBrokers(self):
        fnames = ["Goldman", "Edward", "James", "Luis", "Alexander", "Walter", "Eugene", "Mary", "Morgan", "Jane", "Elizabeth", "Xavier", "Hayden", "Samuel", "Lee"]
        names = ["Johnson", "Rothschild", "Sachs", "Stanley", "Hepburn", "Brown", "McColl", "Fischer", "Edwards", "Becker", "Witter", "Walker", "Lambert", "Smith", "Montgomery", "Lynch", "Roosevelt", "Lehman"]
        locations = ["Earth", "Luna", "Mars", "Saturn", "Jupiter", "Uranus", "Pluto", "Europa", "Io", "Phobos", "Deimos", "Space", "Venus", "Neptune", "Mercury", "Kalliope", "Ganymede", "Callisto", "Amalthea", "Himalia"]
        first = ["The", "First", "Premier", "Finest", "Prime"]
        company = ["Investments", "Securities", "Corporation", "Bank", "Brokerage", "& Co.", "Brothers", "& Sons", "Investement Firm", "Union", "Partners", "Capital", "Trade", "Holdings"]
        
        i = 1
        
        while i <= 5:
            
            pname = ""
            
            match random.randint(1,5):
                
                case 1:
                    if random.random() <= 0.10:
                        pname = random.choice(first) + " "
                    pname = pname + random.choice(names) + " " + random.choice(company)
                case 2:
                    pname = random.choice(names) + " & " + random.choice(names)
                    
                    if random.random() <= 0.25:
                        pname = pname + " " + random.choice(company)
                case 3:
                    if random.random() <= 0.45:
                        pname = random.choice(first) + " "
                    pname = pname + random.choice(locations) + " " + random.choice(company)
                case 4:
                    if random.random() <= 0.10:
                        pname = "The "
                    pname = pname + random.choice(names) + " " + random.choice(locations) + " " + random.choice(company)
                case 5:
                    if random.random() <= 0.10:
                        pname = "The "
                    pname = pname + random.choice(fnames) + " " + random.choice(names)
                    if random.random() <= 0.10:
                        pname = pname + " " + random.choice(company)
                        
            print(f"Pname > {pname}")
            if pname in self.stockBrokers:
                pass
            else:
                self.stockBrokers.append(pname)
                # Iterator DO NOT FORGET
                i = i + 1
                
    def generateStocks(self, amt = 15):
        fruits  = ["Banana", "Strawberry", "Watermelon", "Maracuja", "Pomegranate", "Papaya", "Mango", "Tomato", "Conkerberry", "Fig", "Lychee", "Mandarin", "Oroblanco", "Pumpkin", "Rhubarb", "Tamarillo", "Yantok", "Ziziphus"]
        tech_prefix  = ["Nano", "Cyber", "Funk", "Astro", "Fusion", "Tera", "Exo", "Star", "Virtual", "Plasma", "Robust", "Bit", "Butt"]
        tech_short  = ["soft", "tech", "prog", "tec", "tek", "ware", "", "gadgets", "nics", "tric", "trasen", "tronic", "coin"]
        random_nouns  = ["Johnson", "Cluwne", "General", "Specific", "Master", "King", "Queen", "Wayne", "Rupture", "Dynamic", "Massive", "Mega", "Giga", "Certain", "Stale", "State", "National", "International", "Interplanetary", "Sector", "Planet", "Burn", "Robust", "Exotic", "Solar", "Cheesecake"]
        company  = ["Company", "Factory", "Incorporated", "Industries", "Group", "Consolidated", "GmbH", "LLC", "Ltd", "Inc.", "Association", "Limited", "Software", "Technology", "Programming", "IT Group", "Electronics", "Nanotechnology", "Farms", "Stores", "Mobile", "Motors", "Electric", "Energy", "Pharmaceuticals", "Communications", "Wholesale", "Holding", "Health", "Machines", "Astrotech", "Gadgets", "Kinetics"]
        
        for i in range(1,amt):
            S = stock_tickers.Ticker()
            
            sname = ""
            
            match random.randint(1,6):
                case 1:
                    while(sname == "" or sname == "FAG"):
                        sname = random.choice(consonants_upper) + random.choice(vowels_upper) + random.choice(consonants_upper)
                case 2:
                    sname = random.choice(tech_prefix) + random.choice(tech_short)
                    if random.random() <= 0.20:
                        sname = sname + " " + random.choice(company)
                case 3 | 4:
                    fruit = random.choice(fruits)
                    fruits.remove(fruit)
                    if random.random() <= 0.10:
                        sname = "The "
                    sname = sname + fruit
                    
                    if random.random() <= 0.40:
                        sname = sname + " " + random.choice(company)
                    
                case 5 | 6:
                    pname = random.choice(random_nouns)
                    random_nouns.remove(pname)
                    
                    match random.randint(1,3):
                        case 1:
                            sname = f"{pname} & {pname}"
                        case 2:
                            sname = f"{pname} {random.choice(company)}"
                        case 3:
                            sname = pname
            S.name = sname
            S.short_name = self.generateDesignation(S.name)
            S.current_value = random.randint(10, 125)
            dv = random.randint(10, 40) / 10
            S.fluctuational_coefficient = 1 / dv if random.random() <= 50 else dv
            S.average_optimism = random.randint(-10, 10) / 100
            S.optimism = S.average_optimism + (random.randint(-40, 40) / 100)
            S.current_trend = random.randint(-200, 200) / 10
            S.last_trend = S.current_trend
            S.disp_value_change = random.randint(-1, 1)
            S.speculation = random.randint(-20, 20)
            S.average_shares = math.floor(random.randint(500, 10000) / 10)
            S.outside_shareholders = random.randint(1000, 30000)
            S.available_shares = random.randint(200000, 800000)
            S.fluctuation_rate = random.randint(6, 20)
            S.generateIndustry()
            S.genereateEvents()
            self.stocks += S
            self.last_read[S] = []
                
    def generateDesignation(self, name):
        if len(name) <= 4:
            return name.upper()
        w = name.split(" ")
        if len(w) >= 2:
            d = ""
            i = 1
            while i <= min(5,len(w)):
                d += chr(ord(w[i])).upper()
                i += 1
            return d
        else:
            i = 2
            while i <= len(name):
                if random.random() <= 100 / i:
                    d += chr(ord(name[i])).upper()
                i += 1
            return d
Market()