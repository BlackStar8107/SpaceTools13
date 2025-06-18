import random
import re

consonants_upper = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]

class Industry:
	name = "Industry"
	tokens = []
	title_templates = ["The brand new %product_name% by %company_name% will revolutionize %industry%", \
																	"%jobs% rejoice as %product_name% hits shelves", \
																	"Does %product_name% threaten to reorganize the %industrial% status quo?"]
	title_templates_neutral = ["%product_name%: as if nothing happened", \
																					"Nothing new but the name: %product_name% not quite exciting %jobs%", \
																					"Same old %company_name%, same old product"]
	title_templates_bad = ["%product_name% shaping up to be the disappointment of the century", \
																			"Recipe for disaster: %company_name% releases %product_name%", \
																			"Atrocious quality - %jobs% boycott %product_name%"]
	title_templates_ooc = ["%company_name% is looking to enter the %industry% playing field with %product_name%", \
																			"%company_name% broadens spectrum, %product_name% is their latest and greatest"]
	subtitle_templates = ["%author% investigates whether or not you should invest!", \
																			"%outlet%'s very own %author% takes it to the magnifying glass", \
																			"%outlet% lets you know if you should use it", \
																			"Read our top tips for investors", \
																			"%author% wants you to know if it's a safe bet to buy"]
	
	def generateProductName(self, company_name):
		return
	
	def generateInCharacterProductArticle(self, product_name, S):
		A = None # TODO: Add Articles
		add_tokens = {"company_name" : S.name, "product_name" : product_name, "outlet" : A.outlet, "author" : A.author}
		A.about = S
		A.opinion = random.randint(-1, 1)
		A.subtitle = A.detokenize(random.choice(self.subtitle_templates), self.tokens, add_tokens)
		
		article = "%company_name% %expand_influence% %industry%. [ucfirst(product_name)] %hit_shelves% %this_time% "
		
		if A.opinion > 0:
			A.headline = A.detokenize(random.choice(self.title_templates), self.tokens, add_tokens)
			article += "but %positive_outcome%, %signifying% the %resounding% %success% the product is. The %stock_market% is %excited% over this %development%, and %stockholder% optimism is expected to %rise% as well as the stock value. Our advice: %buy%."
			
		elif A.opinion == 0:
			A.headline = A.detokenize(random.choice(self.title_templates_neutral), self.tokens, add_tokens)
			article += "but %neutral_outcome%. For the average %stockholder%, no significant change on the market will be apparent over this %development%. Our advice is to continue investing as if this product was never released."
		else:
			A.headline = A.detokenize(random.choice(self.title_templates_bad), self.tokens, add_tokens)
			article += "but %negative_outcome%. Following this %complete% %failure%, %stockholder% optimism and stock value are projected to %dip%. Our advice: %sell%."
		A.article = A.detokenize(article, self.tokens, add_tokens)
		
	def detokenise(self, str):
		for T in self.tokens:
			str = re.sub(str, f"%{T}%", random.choice(self.tokens[T]))
		return str
	
class Agriculture(Industry):
	def __init__(self):
		name = "Agriculture"
		tokens = {
			"industry" : ["agriculture", "farming", "agronomy", "horticulture"],
			"industrial" : ["agricultural", "agronomical", "agrarian", "horticultural"],
			"jobs" : ["farmers", "agricultural experts", "agricultural workers", "combine operators"]
		}

		title_templates = ["The brand new %product_name% by %company_name% will revolutionize %industry%", 
										"%jobs% rejoice as %product_name% hits shelves", 
										"Does %product name% threaten to reorganize the %industrial% status quo?", 
										"Took it for a field trip: our first %sneak_peek% of %product_name%.", 
										"Reaping the fruits of %product_name% - %sneak_peek% by %author%", 
										"Cultivating a new %industrial% future with %product_name%", 
										"%company_name% grows and thrives: %product_name% now on the farmer's market", 
										"It's almost harvest season: %product_name% promises to ease your life", 
										"Become the best on the farmer's market with %product_name%", 
										"%product_name%: a gene-modified reimagination of an age-old classic"]

		title_templates_ooc = ["%company_name% is looking to enter the %industry% playing field with %product_name%", 
											"A questionable decision: %product_name% grown on the soil of %company_name%", 
											"%company_name% broadens spectrum, %product_name% is their latest and greatest", 
											"Will %company_name% grow on %industrial% wasteland? Owners of %product_name% may decide", 
											"%company_name% looking to reap profits off the %industrial% sector with %product_name%"]

	def generateProductName(company_name):
		products = ["combine harvester", "cattle prod", "scythe", "plough", "sickle", "cloche", "loy", "spade", "hoe"]
		prefix = ["[company_name]'s ", "the [company_name] ", "the fully automatic ", "the full-duplex ", "the semi-automatic ", "the drone-mounted ", "the industry-leading ", "the world-class "]
		suffix = [" of farming", " multiplex", " +[rand(1,15)]", " [pick(consonants_upper)][rand(1000, 9999)]", " hybrid", " maximus", " extreme"]
		return random.choice(prefix) + random.choice(products) + random.choice(suffix)


class IT(Industry):
	def __init__(self):
		name = "Information Technology"
		tokens = {
					"industry" : ["information technology", "computing", "computer industry"], 
					"industrial" : ["information technological", "computing", "computer industrial"], 
					"jobs" : ["coders", "electricians", "engineers", "programmers", "devops experts", "developers"]
				}

	def latin_number(self, n):
		if (n < 20 or not (n % 10)):
			if (0): return "Nihil"
			if (1): return "Unus"
			if (2): return "Duo"
			if (3): return "Tres"
			if (4): return "Quattour"
			if (5): return "Quinque"
			if (6): return "Sex"
			if (7): return "Septem"
			if (8): return "Octo"
			if (9): return "Novem"
			if (10): return "Decim"
			if (11): return "Undecim"
			if (12): return "Duodecim"
			if (13): return "Tredecim"
			if (14): return "Quattourdecim"
			if (15): return "Quindecim"
			if (16): return "Sedecim"
			if (17): return "Septdecim"
			if (18): return "Duodeviginti"
			if (19): return "Undeviginti"
			if (20): return "Viginti"
			if (30): return "Triginta"
			if (40): return "Quadriginta"
			if (50): return "Quinquaginta"
			if (60): return "Sexaginta"
			if (70): return "Septuaginta"
			if (80): return "Octoginta"
			if (90): return "Nonaginta"
		else:
			return f"{latin_number(n - (n % 10))} {lowertext(latin_number(n % 10))}"

	def generateProductName(company_name):
		products = ["computer", "laptop", "keyboard", "memory card", "display", "operating system", "processor", "graphics card", "nanobots", "power supply"]
		prefix = ["the [company_name] ", "the high performance ", "the mobile ", "the portable ", "the professional ", "the extreme ", "the incredible ", "the blazing fast ", "the bleeding edge ", null]
		L = random.choice([random.choice(consonants_upper), "Seed ", "Radiant ", "Celery ", "Pentathon ", "Athlete ", "Phantom ", "Semper Fi "])
		N = random.randint(0,99)
		prefix2 = L + N
		if random.random() <= 0.05:
			prefix2 += " " + self.latin_number(N)

		return random.choice(prefix) + prefix2 + random.choice(products)
	
class Communications(Industry):
	def __init__(self):
		name = "Communications"
		tokens = {
			"industry" : ["telecommunications"], 
			"industrial" : ["telecommunicational"], 
			"jobs" : ["electrical engineers", "microengineers"]
		}

	def generateProductName(company_name):
		products = ["mobile phone", "PDA", "tablet computer"]
		prefix = ["the %s " % company_name, "the high performance ", "the mobile ", "the portable ", "the professional ", "the extreme ", "the incredible ", "the blazing fast ", "the bleeding edge ", None]
		J = ["%sPhone " % random.choice(consonants_upper).lower(), "Universe ", "Xperience ", "Next ", "Engin Y ", "Cyborg ", random.pick(consonants_upper)]
		L = random.choice(J)
		N = random.randint(1,99)
		prefix2 = L + N
		if random.random() <= 0.25:
			prefix2 += random.choice([" Tiny", " Mini", " Micro", " Slim", " Water", " Air", " Fire", " Earth", " Nano", " Pico", " Femto", " Planck"])

		return random.choice(prefix) + prefix2 + random.choice(products)
	
class Health(Industry):
	def __init__(self):
		name = "Medicine"
		tokens = {
			"industry" : ["medicine"],
			"industrial" : ["medicinal"],
			"jobs" : ["doctors", "nurses", "psychologists", "psychiatrists", "diagnosticians"]
		}

	def generateProductName(company_name):
		prefix = ["amino", "nucleo", "nitro", "panto", "meth", "eth", "as", "algo", "coca", "hero", "morph", "trinitro", "prop", "but", "acet", "acyclo", "lansop", "dyclo", "hydro", "oxycod", "vicod"]
		suffix = ["phen", "pirin", "pyrine", "ane", "amphetamine", "prazoline", "ine", "yl", "amine", "aminophen", "one", "ide", "phenate", "anol", "toulene", "glycerine", "vir"]
		uses = ["antidepressant", "analgesic", "anesthetic", "antiretroviral", "antiviral", "antibiotic", "cough drop", "depressant", "hangover cure", "homeopathic", "fertility drug", "hypnotic", "narcotic", "laxative", "multivitamin", "purgative", "relaxant", "steroid", "sleeping pill", "suppository", "traquilizer"]
		return "%s%s, the %s" % (random.choice(prefix), random.choice(suffix), random.choice(uses))
	
class Consumer(Industry):
	def __init__(self):
		name = "Consumer"
		tokens = {
			"industry" : ["shops", "stores"],
			"industrial" : ["consumer industrial"],
			"jobs" : ["shopkeepers", "checkout machine operators", "manual daytime hygiene engineers", "janitors"]
		}
	
	def generateProductName(self, company):
		meat = ["chicken", "beef", "seal", "monkey", "goat", "insect", "pigeon", "human", "walrus", "brullbar", "bear", "horse", "turkey", "pork", "shellfish", "starfish", "mimic", "mystery"]
		qualifier = ["synthetic", "organic", "bio", "diet", "sugar-free", "paleolithic", "homeopathic", "recycled", "reclaimed", "vat-grown"]
		return "the %s %s meat product line" % (random.choice(qualifier), random.choice(meat))