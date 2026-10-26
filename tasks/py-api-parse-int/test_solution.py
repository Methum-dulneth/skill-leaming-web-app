from solution import parse_int_param


def test_valid_number():
    assert parse_int_param("42") == 42
    assert parse_int_param(" 7 ") == 7


def test_invalid_uses_default():
    assert parse_int_param("abc", 5) == 5
    assert parse_int_param("", 3) == 3


def test_none_uses_default():
    assert parse_int_param(None) == 0
