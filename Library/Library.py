def hand_total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)
    
    total += aces
    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1
        
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    """Return True if hand_1 beats hand_2, and False otherwise."""
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    """Return True if hand_1 beats hand_2, and False otherwise."""
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)
    pass

# Check your answer
q3.check()