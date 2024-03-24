def solution(cards):
    group_sizes = []
    used = set()

    for i, card in enumerate(cards, 1):
        if i in used:
            continue

        card_index = i
        group_size = 0

        while card_index not in used:
            used.add(card_index)
            group_size += 1

            card_index = cards[card_index - 1]

        group_sizes.append(group_size)

    group_sizes = sorted(group_sizes, reverse=True)

    return 0 if len(group_sizes) == 1 else group_sizes[0] * group_sizes[1]
