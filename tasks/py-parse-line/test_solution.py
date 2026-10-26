from solution import greet


def test_basic():
    assert greet("Ada,36") == "Hello Ada, next year you'll be 37"


def test_other():
    assert greet("Sam,9") == "Hello Sam, next year you'll be 10"
