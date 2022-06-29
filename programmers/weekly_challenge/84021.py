# https://programmers.co.kr/learn/courses/30/lessons/84021

from collections import deque
from dataclasses import dataclass
from typing import List


@dataclass
class Shape:
    shape: List[List[int]]
    area: int

    def __eq__(self, other) -> bool:
        r, c = len(self.shape), len(self.shape[0])
        other_r, other_c = len(other.shape), len(other.shape[0])

        if r == other_r and c == other_c:
            if all(
                row == other_row
                for row, other_row in zip(self.shape, other.shape)
            ):
                return True

            if all(
                row == other_row[::-1]
                for row, other_row in zip(self.shape, other.shape[::-1])
            ):
                return True

        if r == other_c and c == other_r:
            other_shape = list(
                map(lambda row: list(row)[::-1], zip(*other.shape))
            )

            if all(
                row == other_row
                for row, other_row in zip(self.shape, other_shape)
            ):
                return True

            if all(
                row == other_row[::-1]
                for row, other_row in zip(self.shape, other_shape[::-1])
            ):
                return True

        return False

    def __repr__(self):
        return "\n".join("".join(str(v) for v in row) for row in self.shape)


def collect_shapes_by_identifier(
    field: List[List[int]], *, identifier: int
) -> List[Shape]:
    def satisfied(r: int, c: int) -> bool:
        return (
            0 <= r < len(field)
            and 0 <= c < len(field[0])
            and field[r][c] == identifier
        )

    def collect(r: int, c: int):
        q = deque([(r, c)])
        collected = [(r, c)]
        visited[r][c] = 1

        while q:
            cr, cc = q.popleft()
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = cr + dr, cc + dc
                if not satisfied(nr, nc):
                    continue
                if visited[nr][nc]:
                    continue

                q.append((nr, nc))
                collected.append((nr, nc))
                visited[nr][nc] = 1

        min_r, max_r = r, r
        min_c, max_c = c, c
        for _r, _c in collected:
            min_r = min(min_r, _r)
            max_r = max(max_r, _r)
            min_c = min(min_c, _c)
            max_c = max(max_c, _c)

        _shape = [
            [0 for _ in range(max_c - min_c + 1)]
            for _ in range(max_r - min_r + 1)
        ]
        for _r, _c in collected:
            _shape[_r - min_r][_c - min_c] = 1

        return Shape(_shape, len(collected))

    visited = [[0 for _ in row] for row in field]
    shapes = []
    for r in range(len(field)):
        for c in range(len(field[0])):
            if field[r][c] != identifier or visited[r][c]:
                continue

            shapes.append(collect(r, c))

    return shapes


def calculate_total_overlap(shapes: List[Shape], others: List[Shape]) -> int:
    used = [0 for _ in shapes]
    others_used = [0 for _ in others]

    total_overlap = 0
    for i, shape in enumerate(shapes):
        for j, other in enumerate(others):
            if used[i] or others_used[j]:
                continue
            if shape != other:
                continue

            total_overlap += shape.area
            used[i] = 1
            others_used[j] = 1

    return total_overlap


def solution(game_board: List[List[int]], table: List[List[int]]) -> int:
    empty_shapes = collect_shapes_by_identifier(game_board, identifier=0)
    blocks = collect_shapes_by_identifier(table, identifier=1)

    return calculate_total_overlap(empty_shapes, blocks)
