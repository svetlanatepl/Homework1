import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Позитивные проверки
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("svetlana", "Svetlana"),
    ("how are you", "How are you"),
    ("teplyakova", "Teplyakova"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("whitespace, string", [
    ("  Test1", "Test1"),
    (" Test2 test", "Test2 test"),
    ("/Teplyakova", "/Teplyakova"),
])
def test_trim_positive(whitespace, string):
    assert string_utils.trim(whitespace) == string


@pytest.mark.parametrize("string, symbol", [
    ("Ivan Petrov", "P"),
    ("123abc", "1"),
    ("12 oktober 2025", "5"),
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True


@pytest.mark.parametrize("string, symbol, expected_result", [
    ("Hello world", "world", "Hello "),
    ("1231abc", "1", "23abc"),
])
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result


# Негативные проверки:
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123a", "123a"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("whitespace, string", [
     ("", ""),
])
def test_trim__negative(whitespace, string):
    assert string_utils.trim(whitespace) == string


@pytest.mark.parametrize("string, symbol", [
    ("Ivan Ivanov", "V"),
    ("123_abc", "-"),
    ("cucumber", ""),
    ("cucumber", None),
])
def test_contains_negative(string, symbol):
    with pytest.raises(TypeError):
        assert string_utils.capitalize(string, symbol) is False


@pytest.mark.parametrize("string, symbol, expected_result", [
    ("Hello world", "", "Hello world"),
    ("My name is Svetlana", None, "My name is Svetlana"),
])
def test_delete_symbol_negative(string, symbol, expected_result):
    with pytest.raises(TypeError):
        assert string_utils.delete_symbol(string, symbol) == expected_result
