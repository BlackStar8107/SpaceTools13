import random
import math

# Each of these classes is its own event!!!

class Event:
	def __init__(self, gameTicker):
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
		if self.finished:
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
	
class Product(Event):
	def __init__(self, S, gameTicker):
		self.name = "product"
		self.product_name = ""
		self.product_article = None
		self.effect = 0
		self.company = S
		self.mins = random.randint(5, 20)
		self.next_phase = self.mins * 600 + gameTicker.last_tick_time # TODO: Write ticker fuckery
		self.current_title = "Product demo"
		self.current_desc = S.industry.detokenise(f"{S.name} will unveil a new product on an upcoming %industrial% conference held at spacetime {self.spacetime(self.next_phase)}")
		S.addEvent(self)
		
	def transition(self):
		self.last_change = gameTicker.last_tick_time
		
		match self.phase_id:
			case 0:
				self.next_phase = ticker.round_elapsed_ticks + rand(300, 600) * 10
				self.product_name = company.industry.generateProductName(company.name)
				self.current_title = f"Product release: {product_name}"
				self.current_desc = f"{company.name} unveiled their newest product, {product_name}, at a conference. Product release is expected to happen at spacetime {spacetime(next_phase)}."
				self.product_article = self.company.industry.generateInCharacterProductArticle(self.product_name, self.company)
				self.effect = self.product_article.opinion + random.randint(-1, 1)
				self.company.affectPublicOpinion(effect)
				self.phase_id = 1
			case 1:
				self.finished = 1
				self.hidden = True
				self.company.addArticle(product_article)
				self.effect += self.product_article.opinion * 5
				self.company.affectPublicOpinion(effect)
				self.phase_id = 2
				self.company.generateEvent(type)
		
class Product(Event):

class Arrest(Event):
	def __init__(self, S, gameTicker):
		self.name = "arrest"
		self.female = 0
		self.tname = "Elvis Presley"
		self.position = "CEO"
		self.offenses = "murder"
		self.effect = 0


if __name__ == "__main__":
	# Generate Products
	products = Product()