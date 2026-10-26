from solution import format_log


def test_basic_line():
    assert format_log("get", "/users", 200, 12.34) == "GET /users -> 200 (12.3ms)"


def test_int_ms_gets_decimal():
    assert format_log("post", "/items", 201, 3) == "POST /items -> 201 (3.0ms)"


def test_already_upper():
    assert format_log("DELETE", "/items/9", 404, 0.5) == "DELETE /items/9 -> 404 (0.5ms)"
