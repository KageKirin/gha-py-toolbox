## tuniq

# namespace: tuniq


def unique(ar: list) -> list:
    uniq = []
    [uniq.append(x) for x in ar if x not in uniq]
    return uniq
