import itertools

first      = lambda obj: next(iter(obj))
take       = lambda obj, n: list(itertools.islice(obj        , n))
take_items = lambda obj, n: list(itertools.islice(obj.items(), n))
