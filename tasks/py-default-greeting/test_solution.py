from solution import greet


def test_default():
    assert greet("Sam") == "Hello, Sam!"


def test_custom():
    assert greet("Sam", "Hi") == "Hi, Sam!"
