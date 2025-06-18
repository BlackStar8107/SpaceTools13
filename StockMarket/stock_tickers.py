import random
import pyclbr
import stock_events
import stock_industries
import sys

random.seed()

class Ticker:
	def __init__(self, gameTicker, market):
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
		
		self.gameTicker = gameTicker
		self.market = market
		
	def addEvent(self, E):
		if E not in self.events:
			self.events.append(E)
		else:
			pass
		# self.events = self.events | E
		
	def addArticle(self, A):
		if(A not in self.articles):
			self.articles.insert(0,A)
		else:
			pass
			
	def genereateEvents(self):
		events = pyclbr.readmodule("stock_events")
		for event in events:
			if event != "Event":
				event_class = getattr(stock_events, event)(self, self.gameTicker)
				self.generateEvent(event_class)
				print(self.short_name,":",event_class)
		pass
	
	def generateEvent(self,E):
		self.addEvent(E)
		
	def affectPublicOpinion(self, boost):
		self.optimism += random.random.randintint(0, 500) / 500 * boost
		self.average_optimism += random.random.randintint(0,150) / 5000 * boost
		self.speculation += random.random.randintint(-5, 25) / 10 * boost
		self.performance += random.random.randintint(0, 110) / 100 * boost
		
	def generateIndustry(self):
		# TODO
		if self.name.find("Farms") != -1:
			self.industry = stock_industries.Agriculture()
			print("Assigned %s as Agriculture" % (self.name))

		elif any(x in self.name for x in ["Software","Programming","IT Group","Electronics","Electric","Nanotechnology"]):
			self.industry = stock_industries.IT()
			print("Assigned %s as IT" % (self.name))

		elif self.name.find("Mobile") != -1 | self.name.find("Communications") != -1:
			self.industry = stock_industries.Communications()
			print("Assigned %s as Communications" % (self.name))

		elif self.name.find("Pharmaceuticals") != -1 | self.name.find("Health") != -1:
			self.industry = stock_industries.Health()
			print("Assigned %s as Health" % (self.name))

		elif self.name.find("Wholesale") != -1 | self.name.find("Stores") != -1:
			self.industry = stock_industries.Consumer()
			print("Assigned %s as Consumer" % (self.name))

		else:
			industries = pyclbr.readmodule("stock_industries")
			del industries["Industry"]
			random.randint_ind_name = random.choice(list(industries.keys()))
			random.randint_indust = getattr(stock_industries, random.randint_ind_name)
			self.industry = random.randint_indust()
			print("Assigned %s randomly as %s" % (self.name, random.randint_ind_name))

	def frc(self, amt):
		shares = self.available_shares + self.outside_shareholders * self.average_shares
		fr = amt / 100 / shares * self.fluctuational_coefficient * self.fluctuation_rate * max(-(self.current_trend / 100), 1)

		if (fr < 0 and self.speculation < 0 or fr > 0 and self.speculation > 0):
			fr *= max(abs(self.speculation) / 5, 1)
		else:
			fr /= max(abs(self.speculation) / 5, 1)

		return fr

	def supplyGrowth(self, amt):
		fr = self.frc(amt)
		self.available_shares += amt
		if (abs(fr) < 0.0001):
			return
		self.current_value -= fr * self.current_value

	def supplyDrop(self, amt):
		supplyGrowth(-amt)


	def fluctuate(self):
		change = random.random.randintint(-100, 100) / 10 + optimism * random.randint(200) / 10
		self.optimism -= (self.optimism - self.average_optimism) * (random.randint(10,80) / 1000)
		shift_score = change + self.current_trend

		as_score = abs(shift_score)
		sh_change_dev = random.randint(-10, 10) / 10

		sh_change = shift_score / (as_score + 100) + sh_change_dev
		shareholder_change = round(sh_change)

		self.outside_shareholders += shareholder_change
		share_change = shareholder_change * self.average_shares

		if (as_score > 20 and random() <= (as_score / 4)):
			avg_change_dev = random.randint(-10, 10) / 10

			avg_change = shift_score / (as_score + 100) + avg_change_dev

			average_shares += avg_change
			share_change += outside_shareholders * avg_change


		cv = self.last_value
		self.supplyDrop(share_change)
		self.available_shares += share_change

		if (random.random() <= (0.25)):
			self.average_optimism = clamp(self.average_optimism + (random.randint(-3, 3) - self.current_trend * 0.15) / 100, -1, 1)

		aspec = abs(speculation)
		if (random.random() <= int(str(0.)+str(((aspec - 75) * 2)))):
			self.speculation += random.randint(-2, 2)
		else:
			if (random() <= (0.50)):
				self.speculation += random.randint(-2, 2)
			else:
				self.speculation += random.randint(-200, 0) / 1000 * self.speculation
				if (random() <= (0.1) and random() <= (0.5)):
					self.speculation += random.randint(-2000, 0) / 1000 * self.speculation

		self.current_value += (self.speculation / random.randint(10000, 25000) + self.performance / random.randint(100, 800)) * self.current_value
		if (self.current_value < 5):
			self.current_value = 5

		if (self.performance != 0):
			self.performance = random.randint(900,1050) / 1000 * self.performance
			if (abs(self.performance) < 0.2):
				self.performance = 0

		if cv < self.current_value:
			self.disp_value_change = 1
		elif cv > self.current_value:
			self.disp_value_change = -1
		else:
			self.disp_value_change = 0

		self.last_value = self.current_value
		if (len(self.values) >= 50):
			del values[1]
		values += current_value

		if (self.current_value < 10):
			self.unifyShares()

		self.last_trend = self.current_trend
		self.current_trend += random.randint(-200, 200) / 100 + self.optimism * random.randint(200) / 10 + max(50 - abs(self.speculation), 0) / 50 * random.randint(0, 200) / 1000 * (-self.current_trend) + max(self.speculation - 50, 0) * random.randint(0, 200) / 1000 * self.speculation / 400

	def unifyShares(self):
		for I in self.shareholders:
			shr = self.shareholders[I]
			if (shr % 2):
				sellShares(I, 1)
			shr -= 1
			self.shareholders[I] /= 2
			if (not self.shareholders[I]):
				self.shareholders -= I
		for B in borrow_brokers:
			B.share_amount = round(B.share_amount / 2)
			B.share_debt = round(B.share_debt / 2)
		for B in borrows:
			B.share_amount = round(B.share_amount / 2)
			B.share_debt = round(B.share_debt / 2)
		self.average_shares /= 2
		self.available_shares /= 2
		self.current_value *= 2
		self.last_unification = self.gameTicker.tickcount

	def process(self):
		for borrow in self.borrows:
			if (self.gameTicker.tickcount > borrow.grace_expires):
				modifyAccount(borrow.borrower, -max(self.current_value * borrow.share_debt, 0), 1)
				self.borrows -= borrow
				del borrow
			elif (ticker.round_elapsed_ticks > borrow.lease_expires):
				if (borrow.borrower in self.hareholders):
					amt = self.shareholders[borrow.borrower]
					if (amt >= borrow.share_debt):
						self.shareholders[borrow.borrower] -= borrow.share_debt
						self.borrows -= borrow
						self.modifyAccount(borrow.borrower,borrow.deposit)
						del borrow
					else:
						self.shareholders -= borrow.borrower
						borrow.share_debt -= amt
		if (self.bankrupt):
			return
		for borrow in self.borrow_brokers:
			if (borrow.offer_expires < gameTicker.tickcount):
				self.borrow_brokers -= borrow
				del(borrow)
		if (random.random() <= (1) and random.random() <= (3)):
			self.generateBrokers()
		self.fluctuation_counter += 1
		if (self.fluctuation_counter >= self.fluctuation_rate):
			for E in events:
				E.process()
			fluctuation_counter = 0
			self.fluctuate()

	def generteBrokers(self):
		if (len(self.borrow_brokers) > 2):
			return
		if (not len(self.market.stockBrokers)):
			self.market.generateBrokers()
		broker = random.choice(self.market.stockBrokers)
		B = Borrow()
		B.broker = broker
		B.stock = self
		B.lease_time = random.randint(4, 7) * 600
		B.grace_time = random.randint(1, 3) * 600
		B.share_amount = random.randint(1, 10) * 100
		B.deposit = random.randint(20, 70) / 100
		B.share_debt = B.share_amount
		B.offer_expires = random.randint(5, 10) * 600 + ticker.round_elapsed_ticks
		self.borrow_brokers += B

class Borrow():
	def __init__(self):
		self.broker = ""
		self.borrower = ""
		self.stock = None
		self.lease_expires = 0
		self.lease_time = 0
		self.grace_time = 0
		self.grace_expires = 0
		self.share_amount = 0
		self.share_debt = 0
		self.deposit = 0
		self.offer_expires = 0
		
if __name__ == "__main__":
	thing = Ticker()
	thing.genereateEvents()