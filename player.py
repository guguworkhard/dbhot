from poker import Poker

class Player:

    def __init__(self,nickname):
        self.nickname=nickname
        self.cards=[]

    def get_one_card(self,card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort()

    def show(self):
        """显示玩家手上的牌"""
        print(self.nickname,end=':')
        for card in self.cards:
            print(card,end='')
        print()

def main():
    poker=Poker()
    poker.shuffle()
    nicknames=['gugu','sisi','gusi','sigu']
    players=[Player(nickname) for nickname in nicknames]
    for _ in range(10):
        for player in players:
            card = poker.deal()
            player.get_one_card(card)
    for player in players:
        player.arrange()
        player.show()
    
if __name__=='__main__':
    main()