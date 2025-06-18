import random
import time

class Article():
	def __init(self):
		headline = "Something big is happening"
		subtitle = "Investors panic as stock market collapses"
		article = "God, it's going to be fun to randomly generate this."
		author = "P. Pubbie"
		spacetime = ""
		opinion = 0
		ticks = 0
		about = null
		outlet = ""
		news_outlets = []
		default_tokens = {
			"buy" : ["buy!", "buy, buy, buy!", "get in now!", "to the moon!", "ride the share value to the stars!"], 
			"company" : ["company", "corporation", "conglomereate", "enterprise", "venture"], 
			"complete" : ["complete", "total", "absolute", "incredible"], 
			"country" : ["Space", "Argentina", "Hungary", "United States of America", "United Space", "Space Federation", "Nanotrasen", "The Wizard Federation", "United Kingdom", "Poland", "Denmark", "Sweden", "Serbia", "The European Union", "The Illuminati", "The New World Order", "Eurasian Union", "Asian Union", "United Arab Emirates", "Arabian League", "United States of Africa", "Mars Federation", "Allied Colonies of Jupiter", "Saturn's Ring", "Fringe Republic of Formerly Planet Pluto"], 
			"development" : ["development", "unfolding of events", "turn of events"], 
			"dip" : ["dip", "fall", "rapidly descend", "decrease"], 
			"excited" : ["excited", "euphoric", "exhilarated", "thrilled", "stimulated"], 
			"expand_influence" : ["expands their influence over", "continues to dominate", "looks to gain shares in", "rolls their new product line out in"], 
			"failure" : ["failure", "meltdown", "breakdown", "crash", "defeat", "trainwreck", "wreck"], 
			"famous" : ["famous", "prominent", "leading", "renowned"], 
			"hit_shelves" : ["hit the shelves", "appeared on the market", "came out", "was released"], 
			"industry" : ["industry"], 
			"industrial" : ["industrial"], 
			"jobs" : ["workers"], 
			"negative_outcome" : ["it's not leaving the shelves", "nobody seems to have taken note", "no notable profits have been reported", "it's beginning to look like a huge failure"], 
			"neutral_outcome" : ["it's not lifting off as expected", "it's not selling according to the expectations", "it's only generating enough profit to cover the marketing and manufacturing costs", "it does not look like it will become a massive success"], 
			"positive_outcome" : ["it's already sold out", "it has already sold over one billion units", "suppliers cannot keep up with the wild demand", "several companies using this new technology are already reporting a projected increase in profits"], 
			"resounding" : ["resounding", "tremendous", "total", "massive", "terrific", "colossal"], 
			"rise" : ["rise", "increase", "fly off the positive side of the charts", "skyrocket", "lift off"], 
			"sell" : ["sell!", "sell, sell, sell!", "bail!", "abandon ship!", "get out before it's too late!", "evacuate!", "withdraw!"], 
			"signifying" : ["signifying", "indicating", "displaying the sign of", "displaying"], 
			"sneak_peek" : ["review", "sneak peek", "preview"], 
			"stock_market" : ["stock market", "stock exchange"], 
			"stockholder" : ["stockholder", "shareholder"], 
			"success" : ["success", "triumph", "victory"], 
			"this_time" : ["this week", "last week", "this month", "yesterday", "today", "a few days ago"]
		}

		if (not len(self.news_outlets) or (len(self.news_outlets) and !random.random() <= (100 / (len(self.news_outlets) + 1))))
			ON = self.generateOutletName()
			if (!(ON in self.news_outlets))
				self.news_outlets[ON] = []
			self.outlet = ON
		else
			self.outlet = random.choice(self.news_outlets)

		# How we add new authors for news outlets, with decreasing probability to add every article.
		authors = self.news_outlets[outlet]
		if (not len(authors) or (len(authors) and not random.random() <= (100 / (len(authors) + 1))))
			AN = self.generateAuthorName()
			self.news_outlets[outlet] += AN
			self.author = AN
		else
			self.author = random.choice(authors)

	# Returns a random news outlet name
	generateOutletName(self.):
		locations = ["Earth", "Luna", "Mars", "Saturn", "Jupiter", "Uranus", "Pluto", "Europa", "Io", "Phobos", "Deimos", "Space", "Venus", "Neptune", "Mercury", "Kalliope", "Ganymede", "Callisto", "Amalthea", "Himalia"]
		nouns = ["Post", "Herald", "Sun", "Tribune", "Mail", "Times", "Journal", "Report"]
		timely = ["Daily", "Hourly", "Weekly", "Biweekly", "Monthly", "Yearly"]

		match random.randint(1,3):
			case (1):
				return f"The {pick(locations)} {pick(nouns)}"
			case (2):
				return f"The {pick(timely)} {pick(nouns)}"
			case (3):
				return f"{pick(locations)} {pick(timely)}"

	# Returns a random author name
	generateAuthorName(self):
		# TODO: Impliment actual name lists!
		return "Steve Jobs III"
		# match random.randint(1,3):
		# 	case (1):
		# 		return f"{pick(consonants_upper)}. {pick_string_autokey("last.txt")}"
		# 	case (2):
		# 		return "[prob(50) ? pick_string_autokey("first_male.txt") : pick_string_autokey("names/first_female.txt")] [pick(consonants_upper)].[prob(50) ? "[pick(consonants_upper)]. " : null] [pick_string_autokey("names/last.txt")]"
		# 	case (3):
		# 		return "[prob(50) ? pick_string_autokey("first_male.txt") : pick_string_autokey("names/first_female.txt")] \"[prob(50) ? pick_string_autokey("names/first_male.txt") : pick_string_autokey("names/first_female.txt")]\" [pick_string_autokey("names/last.txt")]"

	formatSpacetime(self, ticks)
		ticksc = round(ticks/100)
		ticksc = ticksc % 100000
		ticksp = f"{ticksc}"
		while (len(ticksp) < 5)
			ticksp = f"0{ticksp}"
		spacetime = f"{ticksp}{time2text(world.realtime, "MM")}{time2text(world.realtime, "DD")}{CURRENT_SPACE_YEAR}"

	formatArticle()
		if (spacetime == "")
			formatSpacetime()
		. = "<div class='article'><div class='headline'>[headline]</div><div class='subtitle'>[subtitle]</div><div class='article-body'>[article]</div><div class='author'>[author]</div><div class='timestamp'>[spacetime]</div></div>"

	# Replaces %tokens% in the string with the various default, industry, or product tokens.
	detokenize(token_string, list/industry_tokens, list/product_tokens = )
		T_list = default_tokens.Copy()
		for (I in industry_tokens)
			T_list[I] = industry_tokens[I]
		for (I in product_tokens)
			T_list[I] = list(product_tokens[I])
		for (I in T_list)
			token_string = replacetext(token_string, "%[I]%", pick(T_list[I]))
		return ucfirst(token_string)
