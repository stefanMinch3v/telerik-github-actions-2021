def sum(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError('Input cannot be less than 0')
    return n1 + n2

def test_sum()   ->   None:
    assert sum(1, 1) == 2
