SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return self.__rank == other.rank_index and self.__suit == other.suit_index 

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"