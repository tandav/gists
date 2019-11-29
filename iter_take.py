import itertools

take       = lambda obj, n: list(itertools.islice(obj        , n))
take_items = lambda obj, n: list(itertools.islice(obj.items(), n))
