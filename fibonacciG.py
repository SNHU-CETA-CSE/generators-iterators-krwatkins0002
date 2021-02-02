def fibogenerator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
