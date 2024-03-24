def solution(s):
    s = s.lower()
    jaden_cased = ""

    following_blank = True

    for c in s:
        if c == " ":
            following_blank = True
        elif following_blank:
            c = c.upper()
            following_blank = False

        jaden_cased += c

    return jaden_cased
