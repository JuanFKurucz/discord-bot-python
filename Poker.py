from itertools import combinations 
import random
from Player import Player

class Poker():
    players = []
    cards = []
    tableCards = []

    def loadCards():
        numbers = list(range(2,14))
        letters = ["d","h","s","c"]
        return [letter+str(number) for letter in letters for number in numbers]

    def __init__(self,players):
        self.players = players
        self.cards = Poker.loadCards()
    
    def getCard(self):
        element = random.choice(self.cards)
        self.cards.remove(element)
        return element

    def start(self):
        for p in self.players:
            for i in range(2):
                p.addCard(self.getCard())
    
    def next(self):
        if len(self.tableCards) == 0:
            for i in range(3):
                self.tableCards.append(self.getCard())
            return None
        elif len(self.tableCards)>=5:
            return self.finish()
        else:
            self.tableCards.append(self.getCard())
            return None
    
    def finish(self):
        maxPlayers = []
        maxScore = 0
        for player in self.players:
            score = player.getScore(self.tableCards)
            if score>maxScore:
                maxPlayers = [player]
                maxScore = score
            elif score == maxScore:
                maxPlayers.append(player)
        return maxPlayers
        





