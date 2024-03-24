import sys

sys.setrecursionlimit(10000)


def solution(nodeinfo):
    nodes = sorted([(*node, n) for n, node in enumerate(nodeinfo, 1)])

    preorder, postorder = [], []

    def dfs(nodes):
        if not nodes:
            return

        root_index = max(range(len(nodes)), key=lambda i: nodes[i][1])

        preorder.append(nodes[root_index][2])

        dfs(nodes[:root_index])
        dfs(nodes[root_index + 1:])

        postorder.append(nodes[root_index][2])

    dfs(nodes)

    return [preorder, postorder]
