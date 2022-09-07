import random

def deal():
    '''return random cards from deck for user and computer'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return 'DRAW'
    elif user_score==0:
        return "win with a blackjack"
    elif computer_score==0:
        return 'lose, opponent has a blackjack'
    elif user_score>21:
        return 'you lose , you went over'
    elif computer_score>21:
        return 'you win , opponent went over'
    elif user_score>computer_score:
        return 'you win as u have greater no.'
    else:
        return 'you lose'

def play_game():
    logo = """
            .------.            _     _            _    _            _    
            |A_  _ |.          | |   | |          | |  (_)          | |   
            |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
            | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
            |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
            `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                |  \/ K|                            _/ |                
                `------'                           |__/           
         """
    print(logo)
    user_card=[]
    computer_card=[]
    game_over=False
    for c in range(2):
        user_card.append(deal())
        computer_card.append(deal())

    while not game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f'user card is {user_card} and users score is {user_score}')
        print(f'computer first card is {computer_card[0]}')

        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True

        else:
            continue_deal=input('type "y" to get another card , type "n" to pass :--> ')
            if continue_deal== 'y':
                user_card.append(deal())
            else:
                game_over=True

    while computer_score!=0 and computer_score<17:
        computer_card.append(deal())
        computer_score=calculate_score(computer_card)
    print(f'your final hand is {user_card} and your score is {user_score}')
    print(f'computer final hand is {computer_card} and computer score is {computer_score}')

    print(compare(user_score,computer_score))


while input('enter "y" if you want to play again and enter "n" if you want to exit :--> ')=="y":
    play_game()



