import pytest
from tests.output_parser import parse_output
from gendiff.gendiff import generate_diff


JSON_INPUT_PATH1 = "tests/fixtures/input1.json"
JSON_INPUT_PATH2 = "tests/fixtures/input2.json"
YAML_INPUT_PATH1 = "tests/fixtures/input1.yml"
YAML_INPUT_PATH2 = "tests/fixtures/input2.yaml"
OUTPUT_PATH1 = "tests/fixtures/output1.txt"
OUTPUT_PATH2 = "tests/fixtures/output2.txt"


expected1 = parse_output(OUTPUT_PATH1)
expected2 = parse_output(OUTPUT_PATH2)


@pytest.mark.parametrize("test_inputs, expected", [
        ((JSON_INPUT_PATH1, JSON_INPUT_PATH2), expected1),
        ((JSON_INPUT_PATH2, JSON_INPUT_PATH1), expected2),
        ((YAML_INPUT_PATH1, YAML_INPUT_PATH2), expected1),
        ((YAML_INPUT_PATH2, YAML_INPUT_PATH1), expected2),
        ((JSON_INPUT_PATH1, YAML_INPUT_PATH2), expected1),
        ((YAML_INPUT_PATH2, JSON_INPUT_PATH1), expected2),
    ])
def test_generate_diff(test_inputs, expected):
    assert generate_diff(*test_inputs) == expected
