# https://leetcode.com/problems/count-number-of-teams/description/

import bisect


class Solution:
    def numTeams(self, rating: list[int]) -> int:
        num_teams = 0

        for i, r in enumerate(rating):
            num_left_lowers = len(list(filter(lambda x: x < r, (left := rating[:i]))))
            num_right_greaters = len(list(filter(lambda x: x > r, (right := rating[i + 1:]))))

            num_teams += num_left_lowers * num_right_greaters

            num_left_greaters = len(list(filter(lambda x: x > r, left)))
            num_right_lowers = len(list(filter(lambda x: x < r, right)))

            num_teams += num_left_greaters * num_right_lowers

        return num_teams

    # from one of best solutions
    def numTeams(self, rating: list[int]) -> int:
        num_soldiers = len(rating)

        soldier_ids = []
        num_teams = 0

        for soldier_id in sorted(range(num_soldiers), key=rating.__getitem__):
            # if ratings are not unique, should use bisect_right
            num_left_lowers = bisect.bisect(soldier_ids, soldier_id)
            num_left_greaters = soldier_id - num_left_lowers
            num_right_lowers = len(soldier_ids) - num_left_lowers
            num_right_greaters = num_soldiers - 1 - len(soldier_ids) - num_left_greaters

            num_teams += num_left_lowers * num_right_greaters + num_left_greaters * num_right_lowers

            soldier_ids.insert(num_left_lowers, soldier_id)

        return num_teams
