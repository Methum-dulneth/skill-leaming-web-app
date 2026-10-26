import pytest
from solution import paginate


def test_last_partial_page():
    r = paginate(list(range(25)), 3, 10)
    assert r == {"items": [20, 21, 22, 23, 24], "page": 3, "total_pages": 3}


def test_first_page_default():
    assert paginate(list(range(5)), per_page=2)["items"] == [0, 1]


def test_past_end_and_empty():
    assert paginate([1, 2, 3], 5, 2)["items"] == []
    assert paginate([], 1, 10)["total_pages"] == 0


def test_bad_page():
    with pytest.raises(ValueError):
        paginate([1, 2], 0)
