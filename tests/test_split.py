from strsplit import split, SplitByStr, SplitByLength  # , SplitByAnyChar


def always_false(_: str) -> bool:
    return False


def always_true(_: str) -> bool:
    return True

# Test SplitByStr splitter


def test_split_by_str_basic():
    splitter = SplitByStr(",")
    text = "a,b,c,d"
    result = split(text, splitter)
    assert list(result) == ["a", "b", "c", "d"]


def test_split_by_str_maxsplit():
    splitter = SplitByStr(delimiter=",", maxsplit=2)
    text = "a,b,c,d"
    result = split(text, splitter)
    assert list(result) == ["a", "b", "c,d"]

# Test SplitByLength splitter


def test_split_by_length_basic():
    splitter = SplitByLength(length=2)
    text = "abcdef"
    result = split(text, splitter)
    assert list(result) == ["ab", "cd", "ef"]


def test_split_by_length_maxsplit():
    splitter = SplitByLength(length=2, maxsplit=2)
    text = "abcdef"
    result = split(text, splitter)
    assert list(result) == ["ab", "cd", "ef"]

# Test SplitByAnyChar splitter


""" def test_split_by_any_char_basic():
    splitter = SplitByAnyChar(chars=" ,;")
    text = "a,b; c d"
    result = split(text, splitter)
    assert result == ["a", "b", "c", "d"]


def test_split_by_any_char_maxsplit():
    splitter = SplitByAnyChar(chars=" ,;", maxsplit=2)
    text = "a,b; c d"
    result = split(text, splitter)
    assert result == ["a", "b", "c d"] """

# Test predicate skipping substrings where predicate is True


def test_split_with_predicate_skips():
    splitter = SplitByStr(delimiter=",")
    text = "a,b,c,d"
    # Predicate to skip 'b' and 'c'
    def predicate(s: str): return s in ("b", "c")
    result = split(text, splitter, predicate=predicate)
    assert list(result) == ["a", "d"]


def test_split_with_predicate_always_true():
    splitter = SplitByStr(delimiter=",")
    text = "a,b,c,d"
    result = split(text, splitter, predicate=always_true)
    assert list(result) == []


def test_split_with_predicate_always_false():
    splitter = SplitByStr(delimiter=",")
    text = "a,b,c,d"
    result = split(text, splitter, predicate=always_false)
    assert list(result) == ["a", "b", "c", "d"]
