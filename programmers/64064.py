import re
from functools import reduce


def solution(user_id, banned_id):
    id_patterns = [re.compile(id_pattern.replace("*", ".")) for id_pattern in banned_id]
    id_candidates = [set() for _ in id_patterns]

    for i, id_pattern in enumerate(id_patterns):
        for uid in user_id:
            if id_pattern.fullmatch(uid) is None:
                continue

            id_candidates[i].add(uid)

    def dfs(index=0, used=set()):
        if index == len(banned_id):
            return {tuple(sorted(used))}
        return reduce(
            lambda l, r: l | r,
            [dfs(index + 1, used | {uid}) for uid in id_candidates[index] - used],
            set()
        )

    return len(dfs())
