# https://programmers.co.kr/learn/courses/30/lessons/72416

from collections import defaultdict
from functools import cache

def solution(sales, links):
    @cache
    def min_sales(node, include_root):
        member_sum = sum(min_sales(member, False) for member in tree[node])
        sales_including_chief = sales[node - 1] + member_sum
        if include_root:
            return sales_including_chief
        
        sales_without_chief = member_sum + min([
            min_sales(member, True) - min_sales(member, False)
            for member in tree[node]
        ], default=0)
        return min(sales_including_chief, sales_without_chief)

    tree = defaultdict(list)
    for chief, member in links:
        tree[chief].append(member)

    return min(min_sales(1, include_root=True), min_sales(1, include_root=False))
