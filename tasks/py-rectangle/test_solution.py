from solution import rectangle_stats


def test_stats():
    assert rectangle_stats(3, 4) == {"area": 12, "perimeter": 14}


def test_square():
    assert rectangle_stats(5, 5) == {"area": 25, "perimeter": 20}
