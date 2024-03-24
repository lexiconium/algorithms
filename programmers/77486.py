from collections import defaultdict


def solution(enroll, referral, seller, amount):
    tree = defaultdict(lambda: {"referral": None, "profit": 0})

    for name, ref in zip(enroll, referral):
        tree[name]["referral"] = ref

    for name, amnt in zip(seller, amount):
        profit = amnt * 100

        while profit:
            if name == "-":
                tree[name]["profit"] += profit
                break

            tree[name]["profit"] += profit - (next_profit := int(0.1 * profit))
            name, profit = tree[name]["referral"], next_profit

    return [tree[name]["profit"] for name in enroll]
