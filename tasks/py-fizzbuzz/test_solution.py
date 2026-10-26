from solution import fizzbuzz


def test_first_five():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_fifteen():
    assert fizzbuzz(15)[-1] == "FizzBuzz"


def test_length():
    assert len(fizzbuzz(20)) == 20
