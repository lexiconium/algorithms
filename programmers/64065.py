def solution(s):
    s_tuple = []

    for subset in sorted(map(
            lambda subset_str: set(map(
                int,
                subset_str.replace("{", "").replace("}", "").split(",")
            )),
            s.split("},{")
    ), key=lambda subset: len(subset)):
        s_tuple.append(list(subset - set(s_tuple))[0])

    return s_tuple
