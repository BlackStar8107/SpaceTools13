import random
import re

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