import pytest
from tests.fixture_parser import parse_json
from gendiff.diff import get_diff


JSON_PLAIN_PATH1 = "tests/fixtures/plain1.json"
JSON_PLAIN_PATH2 = "tests/fixtures/plain2.json"
JSON_NESTED_PATH1 = "tests/fixtures/nested1.json"
JSON_NESTED_PATH2 = "tests/fixtures/nested2.json"
YAML_PLAIN_PATH1 = "tests/fixtures/plain1.yml"
YAML_PLAIN_PATH2 = "tests/fixtures/plain2.yaml"
YAML_NESTED_PATH1 = "tests/fixtures/nested1.yml"
YAML_NESTED_PATH2 = "tests/fixtures/nested2.yaml"
OUTPUT_PLAIN_PATH1 = "tests/fixtures/plain_diff1.json"
OUTPUT_PLAIN_PATH2 = "tests/fixtures/plain_diff2.json"
OUTPUT_NESTED_PATH1 = "tests/fixtures/nested_diff1.json"
OUTPUT_NESTED_PATH2 = "tests/fixtures/nested_diff2.json"


plain_expected1 = parse_json(OUTPUT_PLAIN_PATH1)
plain_expected2 = parse_json(OUTPUT_PLAIN_PATH2)
nested_expected1 = parse_json(OUTPUT_NESTED_PATH1)
nested_expected2 = parse_json(OUTPUT_NESTED_PATH2)


@pytest.mark.parametrize("test_inputs, expected", [
        ((JSON_PLAIN_PATH1, JSON_PLAIN_PATH2), plain_expected1),
        ((JSON_PLAIN_PATH2, JSON_PLAIN_PATH1), plain_expected2),
        ((YAML_PLAIN_PATH1, YAML_PLAIN_PATH2), plain_expected1),
        ((YAML_PLAIN_PATH2, YAML_PLAIN_PATH1), plain_expected2),
        ((JSON_PLAIN_PATH1, YAML_PLAIN_PATH2), plain_expected1),
        ((JSON_PLAIN_PATH2, YAML_PLAIN_PATH1), plain_expected2),
        ((JSON_NESTED_PATH1, JSON_NESTED_PATH2), nested_expected1),
        ((JSON_NESTED_PATH2, JSON_NESTED_PATH1), nested_expected2),
        ((YAML_NESTED_PATH1, YAML_NESTED_PATH2), nested_expected1),
        ((YAML_NESTED_PATH2, YAML_NESTED_PATH1), nested_expected2),
        ((YAML_NESTED_PATH1, JSON_NESTED_PATH2), nested_expected1),
        ((YAML_NESTED_PATH2, JSON_NESTED_PATH1), nested_expected2),
    ])
def test_get_diff(test_inputs, expected):
    assert get_diff(*test_inputs) == expected
