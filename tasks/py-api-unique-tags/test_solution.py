from solution import collect_tags


def test_dedupes_case_insensitive():
    posts = [{"tags": ["Python", "API"]}, {"tags": ["api", "Flask"]}, {"title": "no tags"}]
    assert collect_tags(posts) == ["api", "flask", "python"]


def test_empty():
    assert collect_tags([]) == []


def test_returns_list():
    assert isinstance(collect_tags([{"tags": ["x"]}]), list)
