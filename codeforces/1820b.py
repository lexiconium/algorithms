# https://codeforces.com/problemset/problem/1820/B

def solve(s: str) -> int:
    if (begin := s.find("1")) == -1:
        return 0
    if (s_len := len(s)) == 1:
        return 1

    max_len = 0

    while begin < s_len:
        end = (begin + 1) % s_len

        while s[end] == "1" and end != begin:
            end = (end + 1) % s_len

        max_len = max(end - begin if end > begin else s_len - begin + end, max_len)

        while s[end] == "0" and end != begin:
            end = (end + 1) % s_len

        if end <= begin:
            break

        begin = end

    if max_len == s_len:
        return s_len * s_len

    def area(m: int) -> int:
        return m * (max_len - m + 1)

    if max_len % 2:
        return area((max_len + 1) // 2)
    return max(area(max_len // 2), area((max_len + 2) // 2))


def main() -> None:
    for _ in range(int(input())):
        print(solve(input()))


if __name__ == "__main__":
    main()
