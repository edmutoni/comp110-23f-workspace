"""Demonstrating While Loops by finding low value in string"""

"""Syntax
while <condition>
    <repeat action"""

cards: str = "5235"
low_card: int = int(cards[0])
#look at each num in string
card_inx: int = 0
while card_inx < 4:
    #check if curent card is less than low card
    current_card: int = int(cards[card_inx])
    if (current_card < low_card):
        #update low card
        low_card = current_card
    card_inx = card_inx + 1
print(low_card)


