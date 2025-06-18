import stockmarket
import time
import statistics
import json
import jsonpickle 

class GameTicker():
	def __init__(self):
		self.tickcount = 1
		self.last_tick_times = []
		self.last_tick_time = 0.0
		self.seconds_per_tick = 0.0
		self.ticks_per_second = 0.0
		self.tick_rate = 1
		self.market = None
		
	def timetick(self):
		# for tick in self.last_tick_time:
		#	 a += tick
		self.seconds_per_tick = statistics.mean(self.last_tick_times) / 1e+9
		self.ticks_per_second = 1 / self.seconds_per_tick
		# print("Seconds per tick >",self.seconds_per_tick)
		# print("Ticks per second >",self.ticks_per_second)
		print(self.tickcount, end="\r")
		
	def tick(self):
		self.tickcount += 1
		if len(self.last_tick_times) >= self.tick_rate:
			self.last_tick_times.pop(0)
			
		lst_time = time.process_time_ns()
		self.last_tick_times.append(lst_time)
		last_tick_time = lst_time
		if self.tickcount % self.tick_rate == 0:
			self.timetick()

	def set_market(self, market):
		self.market = market
			
def dump_obj(obj, level=0):
	for key, value in obj.__dict__.items():
		if not inspect.isclass(value):
			print(" " * level + "%s -> %s" % (key, value))
		else:
			dump_obj(value, level + 2)

if __name__ == "__main__":
	# Inits the "game engine"
	game = GameTicker()
	
	# Generate Businesses
	businesses = stockmarket.Market(game)

	# for i in range(1000):
	# 	game.tick()


	# Log for data gathering purposes
	with open("output.log", "w") as f:

		# Handles the "ticks" and game speed
		for i in range(1000):
			game.tick()

			j = jsonpickle.encode(businesses)
			k = json.dumps(json.loads(j), indent=2)
			# print(k)

			f.write(k)
			 
			# f.write(("#"*55)+"\n")
			# f.write("Tick info:\n")
			# for info in game.__dict__:
			# 	f.write("\t%s > %s\n" % (info, getattr(game,info)))

			# f.write("\nMarket Info:\n")
			# for info in businesses.__dict__:
			# 	f.write("\t%s > %s\n" % (info, getattr(businesses,info)))

			# f.write("\nStock Info:\n")
			# stocks = getattr(businesses,"stocks")
			# for stock in stocks:
			# 	for info in stock.__dict__:
			# 		f.write("\t%s > %s\n" % (info, getattr(stock, info)))
			# 	f.write("\n")