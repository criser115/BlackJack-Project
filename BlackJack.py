import random

deck = {'Kh': 10, 'Ks': 10, 'Kd': 10, 'Kc': 10, 'Qh': 10, 'Qs': 10, 'Qd': 10, 'Qc': 10, 'Jh': 10, 'Js': 10, 'Jd': 10,
        'Jc': 10, '10h': 10, '10s': 10, '10d': 10, '10c': 10, '9h': 9, '9s': 9, '9d': 9, '9c': 9, '8h': 8, '8s': 8,
        '8d': 8, '8c': 8, '7h': 7, '7s': 7, '7d': 7, '7c': 7, '6h': 6, '6s': 6, '6d': 6, '6c': 6, '5h': 5, '5s': 5,
        '5d': 5, '5c': 5, '4h': 4, '4s': 4, '4d': 4, '4c': 4, '3h': 3, '3s': 3, '3d': 3, '3c': 3, '2h': 2, '2s': 2,
        '2d': 2, '2c': 2, 'Ah': 1, 'As': 1, 'Ad': 1, 'Ac': 1}

dealer = []
player_one = []



def hit(new_deck):
    num = len(player_one) + 2
    player_one.append(list(new_deck.items())[num])
    player_one_cards = dict(player_one)
    player_one_sum = sum(player_one_cards.values())
    print(player_one)
    if player_one_sum > 21:
        print("Player One busts with: " + str(player_one_sum))
    else:
        print("Player One has a total of " + str(player_one_sum))
    return player_one_sum


def stand(new_deck, dealer_sum):
    while dealer_sum < 17:
        num = len(player_one) + len(dealer) + 1
        dealer.append(list(new_deck.items())[num])
        dealer_cards = dict(dealer)
        dealer_sum = sum(dealer_cards.values())
        print(dealer)
        if 17 <= dealer_sum <= 20:
            print("Dealer stands with: " + str(dealer_sum))
            print(list(dealer_cards))
            break
        elif dealer_sum == 21:
            print("Dealer Hit Black Jack!")
            print(list(dealer_cards))
            break
        elif dealer_sum > 21:
            print("Dealer Busts with: " + str(dealer_sum))
            print(list(dealer_cards))
            break

    return dealer_sum


def shuffle_deck():
    shuffled_deck = list(deck.items())
    random.shuffle(shuffled_deck)
    d = dict(shuffled_deck)
    return d


def deal():
    new_deck = shuffle_deck()
    player_one.append(list(new_deck.items())[0])
    dealer.append(list(new_deck.items())[1])
    player_one.append(list(new_deck.items())[2])
    dealer.append(list(new_deck.items())[3])

    player_one_cards = dict(player_one)
    dealer_cards = dict(dealer)

    player_one_sum = sum(player_one_cards.values())
    dealer_sum = sum(dealer_cards.values())

    player_one_cards_list = list(player_one_cards.keys())
    dealer_cards_list = list(dealer_cards.keys())

    player_one_card_one, player_one_card_two = [player_one_cards_list[i] for i in (0, 1)]
    dealer_card_one, dealer_card_two = [dealer_cards_list[i] for i in (0, 1)]

    print("Player one cards are " + player_one_card_one + " & " + player_one_card_two + " for a total of " +
          str(player_one_sum))
    print("The Dealer first card is " + dealer_card_one)

    while True:
        if dealer_sum == 21 and dealer_sum > player_one_sum:
            print("Dealer hit Black Jack! You lose!!!")
            break
        elif dealer_sum == 21 and player_one_sum == 21:
            print("Its a push!")
            break
        else:
            user_input = input("Do you want to Hit or Stand? ")
            if user_input == "Hit":
                player_one_sum = hit(new_deck)
                if player_one_sum > 21:
                    break
            elif user_input == "Stand":
                dealer_sum = stand(new_deck, dealer_sum)
                if 16 < dealer_sum < 21:
                    print("The dealer has " + str(dealer_sum))
                    
                break

    if player_one_sum > 21:
        print(dealer_cards_list)
        print("The Dealer Wins!")
    elif dealer_sum > 21:
        print("Player One Wins!")
    elif 21 >= player_one_sum > dealer_sum:
        print("Player One Wins!")
    elif 21 >= dealer_sum > player_one_sum:
        print("Dealer Wins!")
    else:
        print("Its a push.")


deal()