class Rules():
    def createCard(typeC,number):
        return typeC+str(number)
     
    def royalFlush(typeC,cards):
        #royal flush 14,13,12,11,10 from the same type
        if len(cards)<5:
            return False
        cardsNeeded = [
            Rules.createCard(typeC,14),
            Rules.createCard(typeC,13),
            Rules.createCard(typeC,12),
            Rules.createCard(typeC,11),
            Rules.createCard(typeC,10)
        ]
        for card in cardsNeeded:
            if not (card in cards):
                return False
        return True

    def addCardValues(allCards):
        return sum([int(x[1:]) for x in allCards])

    def calculateScore(cards,tableCards):
        allCards = cards+tableCards
        sameType = list(filter(lambda x: x[0]==allCards[0][0],allCards))

        score = 0

        if len(sameType) == 5:
            if royalFlush(allCards[0][0],sameType):
                score = 1000
            else:
                #straightFLush all cards of the same type
                score = 900

        score += Rules.addCardValues(allCards)
        return score
        #for typeCard in ["c","d","h","s"]:
            
        


