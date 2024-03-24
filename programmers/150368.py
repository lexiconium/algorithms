def solution(users, emoticons):
    def dfs(discount_rates=tuple()):
        if len(discount_rates) == len(emoticons):
            user_spent = [
                sum(
                    (100 - r) * cost / 100
                    for r, cost in zip(discount_rates, emoticons)
                    if r >= r_thresh
                )
                for r_thresh, _ in users
            ]

            user_spent = [
                spent for spent, (_, s_thresh) in zip(user_spent, users)
                if spent < s_thresh
            ]

            return len(users) - len(user_spent), sum(user_spent)

        return max(dfs(discount_rates + (r,)) for r in (10, 20, 30, 40))

    return dfs()
