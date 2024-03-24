class Node:
    def __init__(self, index):
        self.prev = index - 1
        self.next = index + 1
        self.active = True


def solution(n, k, cmd):
    nodes = [Node(i) for i in range(n)]
    nodes[0].prev, nodes[-1].next = None, None

    inactives = []

    for c in cmd:
        if c[0] == "C":
            node = nodes[k]

            if node.prev is not None:
                nodes[node.prev].next = node.next

            if node.next is not None:
                nodes[node.next].prev = node.prev

            node.active = False
            inactives.append(k)

            k = node.prev if node.next is None else node.next

        elif c[0] == "Z":
            node = nodes[(l := inactives.pop())]

            if node.prev is not None:
                nodes[node.prev].next = l

            if node.next is not None:
                nodes[node.next].prev = l

            nodes[l].active = True

        elif c[0] == "U":
            _, d = c.split()

            for _ in range(int(d)):
                k = nodes[k].prev
        else:
            _, d = c.split()

            for _ in range(int(d)):
                k = nodes[k].next

    return "".join("O" if node.active else "X" for node in nodes)
