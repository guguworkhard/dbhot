import random
from card import Card
    
class Poker:
    """扑克类"""
    def __init__(self):
        self.cards = [Card(suite,face) for suite in 'ABCD' for face in range(1,14)]

    def shuffle(self):
        """洗牌"""
        self.counter = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.counter]
        self.counter +=1
        return card
    
    def has_more(self):
        """是否还有牌"""
        return self.counter < len(self.cards)


def main():
    poker = Poker()
    poker.shuffle()
    while poker.has_more:
        print(poker.deal(),end='')

if __name__=='__main__':
    main()