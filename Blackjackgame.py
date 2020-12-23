

deck={"Ace of hearts":[1,11],"Queen of hearts":10 ,"King of hearts":10,"Jack of hearts":10,"One of hearts":1,"Two of hearts":2,"three of hearts":3,"Four of hearts":4}

def card_distribution():
    import random
    global dealer_1
    global dealer_2
    global num_1
    global num_2
    global value_1
    global value_2
    global d_sum
    global d_value_1
    global d_value_2
    print("Player's HAND :\n")
    num_1=random.choice(list(deck.keys()))
    print(num_1)
    if num_1=="Ace of hearts" :
        value_1=deck["Ace of hearts"][1]
    else:
        value_1=deck.get(num_1)
    deck.pop(num_1)
    num_2=random.choice(list(deck.keys()))
    print(num_2)
    if num_2=="Ace of hearts" :
        value_2=deck["Ace of hearts"][1]
    else:
        value_2=deck.get(num_2)
    deck.pop(num_2)
    print("\n")
    global sum
    sum=value_1+value_2
    print("Dealer's Hand :\n")
    dealer_1=random.choice(list(deck.keys()))
    
    if dealer_1=="Ace of hearts" :
        d_value_1=deck["Ace of hearts"][1]
    else:
        d_value_1=deck.get(dealer_1)
    print("<Card hidden>")
    print(dealer_1)
    deck.pop(dealer_1)
    dealer_2=random.choice(list(deck.keys()))
    if dealer_2=="Ace of hearts" :
        d_value_2=deck["Ace of hearts"][1]
    else:
        d_value_2=deck.get(dealer_2)
   
    print(dealer_2)
    deck.pop(dealer_2)
    d_sum=d_value_1+d_value_2
    if d_sum==21 :
        print("Dealer wins")
        play_again()



    player_check()
    


def player_hit() :
    global sum
    import random 

    option=input("Would you like to HIT or STAND? Enter 'h' or 's' ")
    if option.lower()=="h" :
        num=random.choice(list(deck.keys()))
        print(num)
        if num=="Ace of hearts" and sum<=10 :
            value=deck["Ace of hearts"][1]
        elif num=="Ace of hearts" and sum>10 :
            value=deck["Ace of hearts"][0]
        else:
            value=deck.get(num)
        deck.pop(num)
        sum=sum+value
        player_check()
        
    elif option.lower()=="s" :
        print("your turn is over")
        dealer_chance()
    else:
        print("wrong choice")
        player_hit()


def player_check():
    global bet
    global sum
    if sum>=22:
        print("You are Busted")
        bet=0
        print("you have 0")
        play_again()
    elif sum==21:
        print("you Win!!!")
        bet=bet*2
        print("you won %d"%bet)
        play_again()
    else:
        player_hit()

def dealer_chance():
    global bet
    print("\nDealers Turn ....")
    print(dealer_1)
    print(dealer_2)
    if sum>d_sum :
        print("Player Wins!!!")
        bet=bet*2
        print("you won %d"%bet)
        play_again()
    elif sum==d_sum:
        print("DRAW")
        play_again()

    else:
        print("Dealer Wins!!")
        bet=0
        print("you have %d"%bet)
        play_again()

        
def play_again():
    
    house=input("Would you like to play again?")
    if house.lower()=="y":
        global deck
        deck={"Ace of hearts":[1,11],"Queen of hearts":10 ,"King of hearts":10,"Jack of hearts":10,"One of hearts":1,"Two of hearts":2,"three of hearts":3,"Four of hearts":4}
        bet=int(input("How much bet would you like to place?"))
        print("\n")
        card_distribution()
        player_hit()
        play_again()

        
    else:
        print("thank you for playing")
        exit()
        

    




# Main code

print("Hello!!!\nWelcome to the game of Blackjack..")
print("Try to reach close to sum of 21 before the Dealer.\nAce can be 1 or 11 which evervalue is appropriate\n")
bet=int(input("How much bet would you like to place?"))
print("\n")
card_distribution()
player_hit()
play_again()

