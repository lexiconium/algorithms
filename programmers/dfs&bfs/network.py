# https://programmers.co.kr/learn/courses/30/lessons/43162

def find_root(disjoint_set, node):
    while node != disjoint_set[node]:
        node = disjoint_set[node]
    return node

def solution(n, computers):
    disjoint_set = [m for m in range(n)]
    
    for u, others in enumerate(computers):
        root_u = find_root(disjoint_set, u)
        for v, is_connected in enumerate(others):
            if u == v or not is_connected:
                continue
            root_v = find_root(disjoint_set, v)
            if root_u != root_v:
                disjoint_set[root_v] = root_u
    
    return len(set(disjoint_set))
