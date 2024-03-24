def solution(coin, cards):
    n = len(cards)

    in_hand = set(cards[: n // 3])
    candidates = set()
    num_rounds = 1

    def can_pair(cards_1, cards_2):
        for card_1 in cards_1:
            for card_2 in cards_2:
                if card_1 + card_2 == n + 1:
                    return card_1
        return 0

    for i in range(n // 3, n, 2):
        candidates |= {cards[i], cards[i + 1]}

        if card := can_pair(in_hand, in_hand):
            in_hand -= {card, n + 1 - card}
        elif coin > 0 and (card := can_pair(in_hand, candidates)):
            in_hand.remove(card)
            candidates.remove(n + 1 - card)
            coin -= 1
        elif coin > 1 and (card := can_pair(candidates, candidates)):
            candidates -= {card, n + 1 - card}
            coin -= 2
        else:
            break

        num_rounds += 1

    return num_rounds
