import pytest
from tests.fixture_parser import parse_txt, parse_json
from gendiff.formatters.stylish import stylish


DIFF_PLAIN_PATH1 = "tests/fixtures/plain_diff1.json"
DIFF_PLAIN_PATH2 = "tests/fixtures/plain_diff2.json"
DIFF_NESTED_PATH1 = "tests/fixtures/nested_diff1.json"
DIFF_NESTED_PATH2 = "tests/fixtures/nested_diff2.json"
OUTPUT_PLAIN_PATH1 = "tests/fixtures/plain_stylished1.txt"
OUTPUT_PLAIN_PATH2 = "tests/fixtures/plain_stylished2.txt"
OUTPUT_NESTED_PATH1 = "tests/fixtures/nested_stylished1.txt"
OUTPUT_NESTED_PATH2 = "tests/fixtures/nested_stylished2.txt"


plain_diff1 = parse_json(DIFF_PLAIN_PATH1)
plain_diff2 = parse_json(DIFF_PLAIN_PATH2)
nested_diff1 = parse_json(DIFF_NESTED_PATH1)
nested_diff2 = parse_json(DIFF_NESTED_PATH2)
plain_expected1 = parse_txt(OUTPUT_PLAIN_PATH1)
plain_expected2 = parse_txt(OUTPUT_PLAIN_PATH2)
nested_expected1 = parse_txt(OUTPUT_NESTED_PATH1)
nested_expected2 = parse_txt(OUTPUT_NESTED_PATH2)


@pytest.mark.parametrize("test_input, expected", [
        (plain_diff1, plain_expected1),
        (plain_diff2, plain_expected2),
        (nested_diff1, nested_expected1),
        (nested_diff2, nested_expected2),
    ])
def test_stylished(test_input, expected):
    assert stylish(test_input) == expected
