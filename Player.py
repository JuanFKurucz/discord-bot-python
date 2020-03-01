from Rules import Rules
class Player():
    def __init__(self,id,startingMoney=0):
        self.id=id
        self.money = startingMoney
        self.cards = []
        self.status = False
    
    def addCard(self,card):
        self.cards.append(card)

    def getScore(self,tableCards):
        return Rules.calculateScore(self.cards,tableCards)



