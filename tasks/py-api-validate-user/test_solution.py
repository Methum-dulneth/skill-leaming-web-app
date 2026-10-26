from solution import validate_user

AGE_ERR = "age must be an integer between 0 and 150"


def test_valid_payload():
    assert validate_user({"name": "Ann", "age": 30, "email": "a@b.com"}) == []


def test_empty_payload_all_errors_in_order():
    assert validate_user({}) == ["name is required", AGE_ERR, "email is invalid"]


def test_bool_age_rejected():
    assert validate_user({"name": "Bo", "age": True, "email": "b@c.io"}) == [AGE_ERR]


def test_blank_name_and_out_of_range():
    assert validate_user({"name": "  ", "age": 200, "email": "x"}) == ["name is required", AGE_ERR, "email is invalid"]
