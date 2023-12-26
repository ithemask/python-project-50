import pytest
from tests.fixture_parser import parse_txt
from gendiff.gendiff import generate_diff


JSON_PLAIN_PATH1 = "tests/fixtures/plain1.json"
JSON_PLAIN_PATH2 = "tests/fixtures/plain2.json"
JSON_NESTED_PATH1 = "tests/fixtures/nested1.json"
JSON_NESTED_PATH2 = "tests/fixtures/nested2.json"
YAML_PLAIN_PATH1 = "tests/fixtures/plain1.yml"
YAML_PLAIN_PATH2 = "tests/fixtures/plain2.yaml"
YAML_NESTED_PATH1 = "tests/fixtures/nested1.yml"
YAML_NESTED_PATH2 = "tests/fixtures/nested2.yaml"

OUTPUT_PLAIN_STYLISHED_PATH1 = "tests/fixtures/plain_stylished1.txt"
OUTPUT_PLAIN_STYLISHED_PATH2 = "tests/fixtures/plain_stylished2.txt"
OUTPUT_NESTED_STYLISHED_PATH1 = "tests/fixtures/nested_stylished1.txt"
OUTPUT_NESTED_STYLISHED_PATH2 = "tests/fixtures/nested_stylished2.txt"

OUTPUT_PLAIN_PLAINED_PATH1 = "tests/fixtures/plain_plained1.txt"
OUTPUT_PLAIN_PLAINED_PATH2 = "tests/fixtures/plain_plained2.txt"
OUTPUT_NESTED_PLAINED_PATH1 = "tests/fixtures/nested_plained1.txt"
OUTPUT_NESTED_PLAINED_PATH2 = "tests/fixtures/nested_plained2.txt"

OUTPUT_PLAIN_JSONED_PATH1 = "tests/fixtures/plain_jsoned1.txt"
OUTPUT_PLAIN_JSONED_PATH2 = "tests/fixtures/plain_jsoned2.txt"
OUTPUT_NESTED_JSONED_PATH1 = "tests/fixtures/nested_jsoned1.txt"
OUTPUT_NESTED_JSONED_PATH2 = "tests/fixtures/nested_jsoned2.txt"

plain_stylished_exp1 = parse_txt(OUTPUT_PLAIN_STYLISHED_PATH1)
plain_stylished_exp2 = parse_txt(OUTPUT_PLAIN_STYLISHED_PATH2)
nested_stylished_exp1 = parse_txt(OUTPUT_NESTED_STYLISHED_PATH1)
nested_stylished_exp2 = parse_txt(OUTPUT_NESTED_STYLISHED_PATH2)

plain_plained_exp1 = parse_txt(OUTPUT_PLAIN_PLAINED_PATH1)
plain_plained_exp2 = parse_txt(OUTPUT_PLAIN_PLAINED_PATH2)
nested_plained_exp1 = parse_txt(OUTPUT_NESTED_PLAINED_PATH1)
nested_plained_exp2 = parse_txt(OUTPUT_NESTED_PLAINED_PATH2)

plain_jsoned_exp1 = parse_txt(OUTPUT_PLAIN_JSONED_PATH1)
plain_jsoned_exp2 = parse_txt(OUTPUT_PLAIN_JSONED_PATH2)
nested_jsoned_exp1 = parse_txt(OUTPUT_NESTED_JSONED_PATH1)
nested_jsoned_exp2 = parse_txt(OUTPUT_NESTED_JSONED_PATH2)


@pytest.mark.parametrize("test_inputs, expected", [
    ((JSON_PLAIN_PATH1, JSON_PLAIN_PATH2), plain_stylished_exp1),
    ((JSON_PLAIN_PATH1, JSON_PLAIN_PATH2, "stylish"), plain_stylished_exp1),
    ((JSON_PLAIN_PATH2, JSON_PLAIN_PATH1, "stylish"), plain_stylished_exp2),
    ((YAML_PLAIN_PATH1, YAML_PLAIN_PATH2, "stylish"), plain_stylished_exp1),
    ((YAML_PLAIN_PATH2, YAML_PLAIN_PATH1, "stylish"), plain_stylished_exp2),
    ((JSON_PLAIN_PATH1, YAML_PLAIN_PATH2, "stylish"), plain_stylished_exp1),
    ((YAML_PLAIN_PATH2, JSON_PLAIN_PATH1, "stylish"), plain_stylished_exp2),
    ((JSON_NESTED_PATH1, JSON_NESTED_PATH2, "stylish"), nested_stylished_exp1),
    ((JSON_NESTED_PATH2, JSON_NESTED_PATH1, "stylish"), nested_stylished_exp2),
    ((YAML_NESTED_PATH1, YAML_NESTED_PATH2, "stylish"), nested_stylished_exp1),
    ((YAML_NESTED_PATH2, YAML_NESTED_PATH1, "stylish"), nested_stylished_exp2),
    ((YAML_NESTED_PATH1, JSON_NESTED_PATH2, "stylish"), nested_stylished_exp1),
    ((JSON_NESTED_PATH2, YAML_NESTED_PATH1, "stylish"), nested_stylished_exp2),
    ((JSON_PLAIN_PATH1, JSON_PLAIN_PATH2, "plain"), plain_plained_exp1),
    ((JSON_PLAIN_PATH2, JSON_PLAIN_PATH1, "plain"), plain_plained_exp2),
    ((YAML_PLAIN_PATH1, YAML_PLAIN_PATH2, "plain"), plain_plained_exp1),
    ((YAML_PLAIN_PATH2, YAML_PLAIN_PATH1, "plain"), plain_plained_exp2),
    ((JSON_PLAIN_PATH1, YAML_PLAIN_PATH2, "plain"), plain_plained_exp1),
    ((YAML_PLAIN_PATH2, JSON_PLAIN_PATH1, "plain"), plain_plained_exp2),
    ((JSON_NESTED_PATH1, JSON_NESTED_PATH2, "plain"), nested_plained_exp1),
    ((JSON_NESTED_PATH2, JSON_NESTED_PATH1, "plain"), nested_plained_exp2),
    ((YAML_NESTED_PATH1, YAML_NESTED_PATH2, "plain"), nested_plained_exp1),
    ((YAML_NESTED_PATH2, YAML_NESTED_PATH1, "plain"), nested_plained_exp2),
    ((YAML_NESTED_PATH1, JSON_NESTED_PATH2, "plain"), nested_plained_exp1),
    ((JSON_NESTED_PATH2, YAML_NESTED_PATH1, "plain"), nested_plained_exp2),
    ((JSON_PLAIN_PATH1, JSON_PLAIN_PATH2, "json"), plain_jsoned_exp1),
    ((JSON_PLAIN_PATH2, JSON_PLAIN_PATH1, "json"), plain_jsoned_exp2),
    ((YAML_PLAIN_PATH1, YAML_PLAIN_PATH2, "json"), plain_jsoned_exp1),
    ((YAML_PLAIN_PATH2, YAML_PLAIN_PATH1, "json"), plain_jsoned_exp2),
    ((JSON_PLAIN_PATH1, YAML_PLAIN_PATH2, "json"), plain_jsoned_exp1),
    ((YAML_PLAIN_PATH2, JSON_PLAIN_PATH1, "json"), plain_jsoned_exp2),
    ((JSON_NESTED_PATH1, JSON_NESTED_PATH2, "json"), nested_jsoned_exp1),
    ((JSON_NESTED_PATH2, JSON_NESTED_PATH1, "json"), nested_jsoned_exp2),
    ((YAML_NESTED_PATH1, YAML_NESTED_PATH2, "json"), nested_jsoned_exp1),
    ((YAML_NESTED_PATH2, YAML_NESTED_PATH1, "json"), nested_jsoned_exp2),
    ((YAML_NESTED_PATH1, JSON_NESTED_PATH2, "json"), nested_jsoned_exp1),
    ((JSON_NESTED_PATH2, YAML_NESTED_PATH1, "json"), nested_jsoned_exp2),
])
def test_generate_diff(test_inputs, expected):
    assert generate_diff(*test_inputs) == expected


def test_generate_diff_fail():
    with pytest.raises(ValueError):
        generate_diff(JSON_PLAIN_PATH1, JSON_PLAIN_PATH2, "nice")
