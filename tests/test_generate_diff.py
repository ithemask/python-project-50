import pytest
from tests.fixture_parser import parse_txt
from gendiff.gendiff import generate_diff


FILE_PATH1 = "tests/fixtures/nested1.yml"
FILE_PATH2 = "tests/fixtures/nested2.json"
OUTPUT_PATH1 = "tests/fixtures/nested_stylished1.txt"
OUTPUT_PATH2 = "tests/fixtures/nested_plained1.txt"


expected1 = parse_txt(OUTPUT_PATH1)
expected2 = parse_txt(OUTPUT_PATH2)


@pytest.mark.parametrize("test_inputs, expected", [
        ((FILE_PATH1, FILE_PATH2), expected1),
        ((FILE_PATH1, FILE_PATH2, "stylish"), expected1),
        ((FILE_PATH1, FILE_PATH2, "plain"), expected2),
    ])
def test_generate_diff(test_inputs, expected):
    assert generate_diff(*test_inputs) == expected


def test_generate_diff_fail():
    with pytest.raises(ValueError):
        generate_diff(FILE_PATH1, FILE_PATH2, "nice")
