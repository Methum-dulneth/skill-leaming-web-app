from solution import dedupe_sorted


def test_dedupe():
    assert dedupe_sorted([3, 1, 2, 3, 1]) == [1, 2, 3]


def test_empty():
    assert dedupe_sorted([]) == []
