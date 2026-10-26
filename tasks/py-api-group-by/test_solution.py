from solution import group_by


def test_groups_in_order():
    a1 = {"id": 1, "status": "open"}
    b = {"id": 2, "status": "closed"}
    a2 = {"id": 3, "status": "open"}
    assert group_by([a1, b, a2], "status") == {"open": [a1, a2], "closed": [b]}


def test_missing_key_goes_to_none():
    r = {"id": 4}
    assert group_by([r], "status") == {None: [r]}


def test_empty():
    assert group_by([], "status") == {}
