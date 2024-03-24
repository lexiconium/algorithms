day_per_month = 28
month_per_year = 12


def solution(today, terms, privacies):
    term_dict = {
        term: day_per_month * int(due)
        for term, due in map(lambda term: term.split(), terms)
    }

    def date_to_int(date):
        y, m, d = map(int, date.split("."))
        return day_per_month * month_per_year * y + day_per_month * m + d

    today = date_to_int(today)

    return [
        i
        for i, (date, term) in enumerate(map(lambda info: info.split(), privacies), 1)
        if date_to_int(date) + term_dict[term] <= today
    ]
