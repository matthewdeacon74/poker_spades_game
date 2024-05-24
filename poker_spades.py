# base data
cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')
card_values = {'S2':2,'S3':3,'S4':4,'S5':5,'S6':6,'S7':7,'S8':8,'S9':9,'S10':10,'SJ':11,'SQ':12,'SK':13,'SA':14}


# functions
def check_straight(card1:str, card2:str, card3:str) -> int:
    # create sorted list of cards
    sorted_list = sorted([card_values[card1], card_values[card2], card_values[card3]])
    # check if consecutive, add if they are
    if sorted_list == list(range(sorted_list[0], sorted_list[-1] + 1)):
        return max(sorted_list)
    else:
        return 0


def check_3ofa_kind(card1:str, card2:str, card3:str) -> int:
    if card1 == card2 and card2 == card3:
        return card_values[card1]
    else:
        return 0


def check_royal_flush(card1:str, card2:str, card3:str) -> int:
    result = check_straight(card1, card2, card3)
    if result == 14:
        return result
    else:
        return 0


def play_cards(left1:str, left2:str, left3:str, right1:str, right2:str, right3:str) -> int:
    # check for hands
    flush_check = {'left': check_royal_flush(left1, left2, left3), 'right': check_royal_flush(right1, right2, right3)}
    straight_check = {'left': check_straight(left1, left2, left3), 'right': check_straight(right1, right2, right3)}
    triple_check = {'left': check_3ofa_kind(left1, left2, left3), 'right': check_3ofa_kind(right1, right2, right3)}

    # handle flush (beats all others)
    if 0 < flush_check['left'] and flush_check['right'] == 0:
        return -1
    elif 0 < flush_check['right'] and flush_check['left'] == 0:
        return 1
    elif 0 < flush_check['right'] and flush_check['right'] == flush_check['left']:
        return 0

    # handle straights (beats triples)
    # check if both players got a straight; higher value wins
    if straight_check['left'] > 0 and straight_check['right'] > 0:
        if straight_check['left'] == straight_check['right']:
            return 0
        elif straight_check['left'] > straight_check['right']:
            return -1
        else:
            return 1
    # otherwise straight beats triple or junk
    elif straight_check['left'] > straight_check['right']:
        # left got a straight and right didn't
        return -1
    elif straight_check['right'] > straight_check['left']:
        # right got a straight and left didn't
        return 1

    # handle triples (3 of a kind - beats nothing but garbage)
    if triple_check['left'] > triple_check['right']:
        return -1
    elif triple_check['right'] > triple_check['left']:
        return 1
    else:
        # either both got equal triples, or both hands are garbage
        return 0


# function calls
print(check_straight('S8', 'S9', 'S10'))
print(check_3ofa_kind('SJ', 'SJ', 'SJ'))
print(check_royal_flush('SK', 'SQ', 'SA'))
print(play_cards('S6', 'S6', 'S6', 'S2', 'S3', 'S4'))