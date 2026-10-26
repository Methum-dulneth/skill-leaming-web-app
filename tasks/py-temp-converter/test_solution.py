from solution import c_to_f


def test_freezing():
    assert c_to_f(0) == 32


def test_boiling():
    assert c_to_f(100) == 212


def test_body():
    assert round(c_to_f(37), 1) == 98.6
