def check(cards):
    d = {x: cards.count(x) for x in cards}.values()
    if len(d) == 1:
        return 'Impossible'
    elif len(d) == 2:
        return 'Full House' if 2 in d else 'Four of a Kind'
    elif len(d) == 3:
        return 'Three of a Kind' if 3 in d else 'Two Pairs'
    elif len(d) == 4:
        return 'One Pair',
    else:  # len(d) == 5
        return 'Straight' if max(cards) == min(cards) + 4 else 'Nothing