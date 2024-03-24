import heapq


def solution(n, k, enemy):
    pq = []

    for round_index, num_enemies in enumerate(enemy):
        heapq.heappush(pq, -num_enemies)
        n -= num_enemies

        while n < 0 and k > 0:
            n -= heapq.heappop(pq)
            k -= 1

        if n < 0:
            return round_index

    return len(enemy)
