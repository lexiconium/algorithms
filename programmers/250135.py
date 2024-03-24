def solution(h1, m1, s1, h2, m2, s2):
    def to_sec(h, m, s):
        return 3600 * h + 60 * m + s

    hour_hand_period = to_sec(12, 0, 0)
    min_hand_period = to_sec(0, 60, 0)
    sec_hand_period = 60

    t, t_end = to_sec(h1, m1, s1), to_sec(h2, m2, s2)

    def condition(t_low, t_high, *, low, high, is_last):
        if is_last:
            return t_low == low
        return low <= t_low and t_high < high

    cnt = 0

    while t <= t_end:
        hour_hand_before = (hmod_t := t % hour_hand_period) / hour_hand_period
        hour_hand_after = (hmod_t + 1) / hour_hand_period

        min_hand_before = (mmod_t := t % min_hand_period) / min_hand_period
        min_hand_after = (mmod_t + 1) / min_hand_period

        sec_hand_before = (smod_t := t % sec_hand_period) / sec_hand_period
        sec_hand_after = (smod_t + 1) / sec_hand_period

        if h_added := condition(
            hour_hand_before,
            hour_hand_after,
            low=sec_hand_before,
            high=sec_hand_after,
            is_last=(is_last := t == t_end),
        ):
            cnt += 1

        if m_added := condition(
            min_hand_before,
            min_hand_after,
            low=sec_hand_before,
            high=sec_hand_after,
            is_last=is_last,
        ):
            cnt += 1

        if h_added and m_added and hour_hand_before == min_hand_before:
            cnt -= 1

        t += 1

    return cnt
