from solution import match_route


def test_captures_params():
    assert match_route("/users/<id>/posts/<post_id>", "/users/42/posts/7") == {"id": "42", "post_id": "7"}


def test_static_route_and_trailing_slash():
    assert match_route("/health", "/health/") == {}


def test_literal_mismatch():
    assert match_route("/users/<id>", "/posts/1") is None


def test_length_mismatch():
    assert match_route("/users/<id>", "/users/1/extra") is None
