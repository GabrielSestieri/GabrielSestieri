import random 

suits = ("♥️", '♦️', '♤', '♧')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
            '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True
class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)
                
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
        
class Chips:
    
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        
        except ValueError:
            print("Sorry please provide an integer")
            
        else:
            if chips.bet > chips.total:
                print("Sorry you do not have enough chips to bet. You have: {}".format(chips.total))
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    
    
    while True:
        x = input('Hit or Stand (h/s)? ')
        
        if x[0].lower() == 'h':
            hit(deck, hand)
            
        elif x[0].lower() == 's':
                print("Player stands, Dealer's turn.")
                playing = False
        else:
            print("Sorry, I can only understand entries h or s")
            continue
        
        break
            
            

def show_some(player, dealer):
    print('\nDEALERS HAND:')
    print(' <card hidden>')
    print('',dealer.cards[1])
    print('\nPLAYERS HAND:', *player.cards, sep="\n ")
    

def show_all(player, dealer):
    print("DEALERS HAND: ", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPLAYERS HAND: ", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("DEALER BUSTS, PLAYER WINS!")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player, dealer):
    print('Dealer and player tie! PUSH')


# Set up the Player's chips
player_chips = Chips()

while True:
    # Print an opening statement
    print("Hello and welcome to Blackjack by Gabriel Sestieri")

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    gabriel_hand = Hand()
    gabriel_hand.add_card(deck.deal())
    gabriel_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(gabriel_hand,dealer_hand)
    
    while playing == True:
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, gabriel_hand)

        
        # Show cards (but keep one dealer card hidden)
        show_some(gabriel_hand, dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if gabriel_hand.value > 21:
            player_busts(gabriel_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if gabriel_hand.value <= 21:
        
        while dealer_hand.value < gabriel_hand.value:
            hit(deck, dealer_hand)
    
        # Show all cards
        show_all(gabriel_hand, dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(gabriel_hand, dealer_hand, player_chips)
            
        elif dealer_hand.value > gabriel_hand.value:
            dealer_wins(gabriel_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value < gabriel_hand.value:
            player_wins(gabriel_hand, dealer_hand, player_chips)
        else:
            push(gabriel_hand, dealer_hand)
    
    # Inform Player of their chips total 
    print("\n Player total chips are at: {}".format(player_chips.total))
    # Ask to play again
    if player_chips.total > 0:
        new_game = input("Would you like to play another hand? y/n ")
    
        while new_game[0].lower() != "y" or new_game[0].lower() != "n":
            if new_game[0].lower() == "y":
                playing = True 
                break
            elif new_game[0].lower() == "n":
                print("Thanks for playing!")
                break
            else:
                "Didn't understand try again"
    else:
        print("Sorry you have nothing to play with")
        break
    
    
    
    
deck = Deck()
deck.shuffle()
player = Hand()
player.add_card(deck.deal())
player.add_card(deck.deal())
print(player.cards[0],"+",player.cards[1], "=")
print(player.value)

#print(new_deck.all_cards[-1])