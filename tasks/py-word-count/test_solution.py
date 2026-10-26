from solution import word_count


def test_counts():
    assert word_count("a a b") == {"a": 2, "b": 1}


def test_case():
    assert word_count("The the THE") == {"the": 3}
