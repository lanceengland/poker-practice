from typing import List
from .card import Card
import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Deck:
    def __init__(self):
        self.cards: List[Card] = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def shuffle(self) -> None:
        """Shuffle the deck of cards."""
        random.shuffle(self.cards)
    
    def __str__(self) -> str:
        return ' '.join(str(card) for card in self.cards)
    
    def deal(self) -> Card:
        if not self.cards:
            raise IndexError("Cannot deal from an empty deck")
        return self.cards.pop()
