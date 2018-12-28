# cribbageShowScore.py -- generates and shuffles a standard deck of
# 52 playing cards

import random, itertools

deck = {}

def generateDeck():
    '''This will generate a standard deck of 52 playing cards in a dictionary
    '''
    global deck
    deck = {}
    suits = ['C', 'D', 'H', 'S']
    value = 0
    for suit in suits:
        deck[value] = 'A' + suit
        value += 1
        for i in range(1, 10):
            deck[value] = str(i + 1) + suit
            value += 1
        for letter in ['J', 'Q', 'K']:
            deck[value] = letter + suit
            value += 1

## Not for use with dictionaries
##    for i in range(7):
##        random.shuffle(deck)

    return deck

def getHands(deck):
    '''Returns a hand of four cards, a face up card, and a combination.
    '''
    # Get cards from deck
    hand = random.sample(range(52), 5)
    fullHand = hand.copy()
    faceUp = hand.pop()
    

    return hand, faceUp, fullHand

def scoreValueRunKind(fullHand):
    '''This will return an int score from fullHand utilizing
    itertools powerset. Any number of cards adding up to 15, 2 pts.
    Runs of 3, 4, or 5 cards; 3, 4, 5 pts respectively.
    2, 3, or 4 of a kind; 2, 6, 12 pts respectively.
    '''
    score = 0
    valueHand = fullHand.copy()
    
    # converts cards to point values
    for i in range(len(valueHand)):
        valueHand[i] = (valueHand[i] % 13) + 1
    valueHand.sort()
    
    # if no run after third card, skip
    cardNum = 0
    while cardNum < 3:
        card = valueHand[cardNum]
        if card + 1 in valueHand:
            if card + 2 in valueHand:
                if card + 3 in valueHand:
                    if card + 4 in valueHand:
                        score += 5
                        break
                    else:
                        score += 4
                        break
                else:
                    score += 3
                    break
            else:
                cardNum += 1
        else:
            cardNum += 1

    # find a kind
    uniques = []
    for card in valueHand:
        if card not in uniques:
            uniques.append(card)

    for card in uniques:
        kind = 0
        kind = valueHand.count(card)
        if kind == 4:
            score += 12
            break
        elif kind == 3:
            score += 6
        elif kind == 2:
            score += 2
        

    for i in range(len(valueHand)):
        if valueHand[i] > 10:
            valueHand[i] = 10

    # creates itertools object
    powerValueHand = itertools.chain.from_iterable(itertools.combinations(valueHand, r) for r in range(len(valueHand)
                                                                                                       + 1))
    
    # run through all combinations of cards
    for i in powerValueHand:

        # if the cards add up to 15, 2 pts
        if sum(i) == 15:
            score += 2
            
    return score


def scoreFlushJack(hand, faceUp):

    suits = []
    suit = deck[faceUp][-1]
    score = 0
    
    # cycle through each card and get its suit
    for card in hand:
        suits.append(deck[card][-1])

    # count the occurrence of each suit    
    for shape in ['C', 'D', 'H', 'S']:
        num = suits.count(shape)
        if num == 4:
            if suit in suits:
                score += 5
            else:
                score += 4
    # A Jack of the same suit as the face up card, 1 pt
    for card in hand:
        if deck[card][0] == 'J' and deck[card][-1] == suit:
            score += 1

    return score


## test

generateDeck()

for i in range(20):
    current_hand = []
    hand, faceUp, fullHand = getHands(deck)
    for card in fullHand:
        current_hand.append(deck[card])
    print(current_hand)
    score = scoreValueRunKind(fullHand)
    score += scoreFlushJack(hand, faceUp)
    print(score)
