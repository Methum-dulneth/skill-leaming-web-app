from solution import make_rate_limiter


def test_limit_per_user():
    allow = make_rate_limiter(2)
    assert allow("a") is True
    assert allow("a") is True
    assert allow("a") is False
    assert allow("b") is True


def test_limiters_are_independent():
    l1 = make_rate_limiter(1)
    l2 = make_rate_limiter(1)
    assert l1("u") is True
    assert l2("u") is True
    assert l1("u") is False


def test_zero_limit():
    assert make_rate_limiter(0)("x") is False
