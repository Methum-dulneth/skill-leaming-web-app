from solution import check


def test_mix():
    assert check(10, [5, 15, 10]) == ["low", "high", "correct"]


def test_all_correct():
    assert check(3, [3, 3]) == ["correct", "correct"]
