# gendiff
[![Maintainability](https://api.codeclimate.com/v1/badges/2d017081cd6bac950f2b/maintainability)](https://codeclimate.com/github/ithemask/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2d017081cd6bac950f2b/test_coverage)](https://codeclimate.com/github/ithemask/python-project-50/test_coverage)
[![Actions Status](https://github.com/ithemask/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ithemask/python-project-50/actions)
[![pytest-check](https://github.com/ithemask/python-project-50/actions/workflows/pytest-check.yml/badge.svg)](https://github.com/ithemask/python-project-50/actions/workflows/pytest-check.yml)
[![flake8-check](https://github.com/ithemask/python-project-50/actions/workflows/flake8-check.yml/badge.svg)](https://github.com/ithemask/python-project-50/actions/workflows/flake8-check.yml)
## Description
___gendiff___ _is a simple command-line tool that generates the difference between two configuration files_
## Supported file types
  + _.json_
  + _.yaml_
  + _.yml_
## Available output formats
  + _"stylish" (default):_
    ```
    {
        common: {
          + follow: false
          - setting1: Value 1
          + setting1: {
                key5: value5
            }
          + setting3: {
                key: value
                doge: {
                    wow: so much
                }
            }
        }
        group1: {
          - foo: bar
          - nest: {
                key: value
            }
          + nest: str
        }
    }
    ```
  + _"plain":_
    ```
    Property 'common.follow' was added with value: false
    Property 'common.setting1' was updated. From 'Value 1' to [complex value]
    Property 'common.setting3' was added with value: [complex value]
    Property 'group1.foo' was removed
    Property 'group1.nest' was updated. From [complex value] to 'str'
    ```
  + _"json":_
    ```
    [
      {
        "key": "common",
        "nested": [
          {
            "key": "follow",
            "old value": "nonexistent",
            "new value": false
          },
          {
            "key": "setting1",
            "old value": "Value 1",
            "new value": {
              "key5": "value5"
            }
          },
          {
            "key": "setting3",
            "old value": "nonexistent",
            "new value": {
              "key": "value",
              "doge": {
                "wow": "so much"
              }
            }
          }
        ]
      },
      {
        "key": "group1",
        "nested": [
          {
            "key": "foo",
            "old value": "bar",
            "new value": "nonexistent"
          },
          {
            "key": "nest",
            "old value": {
              "key": "value"
            },
            "new value": "str"
          }
        ]
      }
    ]
    ```
## Requirements
  + _OS Linux_
  + _Python >= 3.9_
  + _Pip >= 22.0_
  + _Poetry >= 1.4_
## Installation
```
git clone git@github.com:ithemask/python-project-50.git
python3 -m pip install --user dist/*.whl
```
## Usage examples
### Displaying the help message
[![asciicast](https://asciinema.org/a/mkyVFtUV17ZiKu6tZ89dlGmaH.svg)](https://asciinema.org/a/mkyVFtUV17ZiKu6tZ89dlGmaH)
### Plain JSON file comparison:
[![asciicast](https://asciinema.org/a/m5PC9PVIPFEJOZINPGhzh0wii.svg)](https://asciinema.org/a/m5PC9PVIPFEJOZINPGhzh0wii)
### Plain YAML file comparison:
[![asciicast](https://asciinema.org/a/7Sug1XmQItCo3qOXCQOTSdsYN.svg)](https://asciinema.org/a/7Sug1XmQItCo3qOXCQOTSdsYN)
### Plain JSON & YAML file comparison:
[![asciicast](https://asciinema.org/a/w9If6nHbTRB9WKPRMXTH1FlYj.svg)](https://asciinema.org/a/w9If6nHbTRB9WKPRMXTH1FlYj)
### Nested JSON file comparison:
[![asciicast](https://asciinema.org/a/JwxSbBbWqqloIiSjAY2Z40gK0.svg)](https://asciinema.org/a/JwxSbBbWqqloIiSjAY2Z40gK0)
### Nested YAML file comparison:
[![asciicast](https://asciinema.org/a/BacX7RIOvdtbwAlxSqfyMQH9I.svg)](https://asciinema.org/a/BacX7RIOvdtbwAlxSqfyMQH9I)
### Nested JSON & YAML file comparison:
[![asciicast](https://asciinema.org/a/lswyzmZLO04RRFVDOTzlK6nzo.svg)](https://asciinema.org/a/lswyzmZLO04RRFVDOTzlK6nzo)
### Choosing the alternative output format
[![asciicast](https://asciinema.org/a/lqKv4iz8PbtDhS4sZBaxIPJmD.svg)](https://asciinema.org/a/lqKv4iz8PbtDhS4sZBaxIPJmD)
[![asciicast](https://asciinema.org/a/CPbVCZHuWra8zD6JcvWhj7OYy.svg)](https://asciinema.org/a/CPbVCZHuWra8zD6JcvWhj7OYy)
