def solution(bandage, health, attacks):
    threshold, recovery, additional = bandage
    max_health = health

    prev_t = 0

    for t, damage in attacks:
        recovered = (dt := t - prev_t - 1) * recovery
        recovered += additional * (dt // threshold)

        health = min(health + recovered, max_health)
        health -= damage

        if health <= 0:
            return -1

        prev_t = t

    return health
