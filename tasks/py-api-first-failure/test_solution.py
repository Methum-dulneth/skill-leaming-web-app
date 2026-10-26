from solution import first_failed_check


def test_skips_private_and_finds_first():
    checks = [("db", True), ("_debug", False), ("cache", False), ("auth", False)]
    assert first_failed_check(checks) == "cache"


def test_all_pass():
    assert first_failed_check([("db", True), ("cache", True)]) is None


def test_empty():
    assert first_failed_check([]) is None
