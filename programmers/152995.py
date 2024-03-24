def solution(scores):
    att_threshold, pr_threshold = scores[0]
    sum_threshold = att_threshold + pr_threshold

    pr_max = 0
    rank = 1

    for att, pr in sorted(scores, key=lambda s: (-s[0], s[1])):
        if att > att_threshold and pr > pr_threshold:
            return -1

        if att + pr > sum_threshold and pr >= pr_max:
            pr_max = pr
            rank += 1

    return rank
