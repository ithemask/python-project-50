# gendiff
[![Maintainability](https://api.codeclimate.com/v1/badges/2d017081cd6bac950f2b/maintainability)](https://codeclimate.com/github/ithemask/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2d017081cd6bac950f2b/test_coverage)](https://codeclimate.com/github/ithemask/python-project-50/test_coverage)
[![Actions Status](https://github.com/ithemask/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ithemask/python-project-50/actions)
[![pytest-check](https://github.com/ithemask/python-project-50/actions/workflows/pytest-check.yml/badge.svg)](https://github.com/ithemask/python-project-50/actions/workflows/pytest-check.yml)
[![flake8-check](https://github.com/ithemask/python-project-50/actions/workflows/flake8-check.yml/badge.svg)](https://github.com/ithemask/python-project-50/actions/workflows/flake8-check.yml)
## Description
___gendiff___ _is a simple command-line tool that generates the difference between two configuration files._  
_Also ___gendiff package___ provides the ___generate_diff___ function that you may use in your projects._  
_For more information see the "Usage examples" section below._
## Supported file types
  + _.json_
  + _.yaml_
  + _.yml_
## Available output formats
  + _"stylish" (default):_
    ```
    {
        common: {
            setting1: Value 1
          - setting2: 200
          + setting3: {
                key5: value5
            }
            setting4: {
                doge: {
                  - wow: 
                  + wow: so much
                }
                key: value
              + ops: vops
            }
        }
      + group1: {
            foo: bar
            baz: bars
        }
    }
    ```
  + _"plain":_
    ```
    Property 'common.setting2' was removed
    Property 'common.setting3' was added with value: [complex value]
    Property 'common.setting4.doge.wow' was updated. From '' to 'so much'
    Property 'common.setting4.ops' was added with value: 'vops'
    Property 'group1' was added with value: [complex value]
    ```
  + _"json":_
    ```
    [
      {
        "key": "common",
        "action": "NESTED",
        "value": [
          {
            "key": "setting1",
            "action": "UNCHANGED",
            "value": "Value 1"
          },
          {
            "key": "setting2",
            "action": "REMOVED",
            "value": 200
          },
          {
            "key": "setting3",
            "action": "ADDED",
            "value": {
              "key5": "value5"
            }
          },
          {
            "key": "setting4",
            "action": "NESTED",
            "value": [
              {
                "key": "doge",
                "action": "NESTED",
                "value": [
                  {
                    "key": "wow",
                    "action": "CHANGED",
                    "value": [
                      "",
                      "so much"
                    ]
                  }
                ]
              },
              {
                "key": "key",
                "action": "UNCHANGED",
                "value": "value"
              },
              {
                "key": "ops",
                "action": "ADDED",
                "value": "vops"
              }
            ]
          }
        ]
      },
      {
        "key": "group1",
        "action": "ADDED",
        "value": {
          "foo": "bar",
          "baz": "bars"
        }
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
make build
make package-install
```
## Usage examples
#### Displaying the help message
[![asciicast](https://asciinema.org/a/mkyVFtUV17ZiKu6tZ89dlGmaH.svg)](https://asciinema.org/a/mkyVFtUV17ZiKu6tZ89dlGmaH)
#### Plain JSON file comparison:
[![asciicast](https://asciinema.org/a/m5PC9PVIPFEJOZINPGhzh0wii.svg)](https://asciinema.org/a/m5PC9PVIPFEJOZINPGhzh0wii)
#### Plain YAML file comparison:
[![asciicast](https://asciinema.org/a/7Sug1XmQItCo3qOXCQOTSdsYN.svg)](https://asciinema.org/a/7Sug1XmQItCo3qOXCQOTSdsYN)
#### Plain JSON & YAML file comparison:
[![asciicast](https://asciinema.org/a/w9If6nHbTRB9WKPRMXTH1FlYj.svg)](https://asciinema.org/a/w9If6nHbTRB9WKPRMXTH1FlYj)
#### Nested JSON file comparison:
[![asciicast](https://asciinema.org/a/JwxSbBbWqqloIiSjAY2Z40gK0.svg)](https://asciinema.org/a/JwxSbBbWqqloIiSjAY2Z40gK0)
#### Nested YAML file comparison:
[![asciicast](https://asciinema.org/a/BacX7RIOvdtbwAlxSqfyMQH9I.svg)](https://asciinema.org/a/BacX7RIOvdtbwAlxSqfyMQH9I)
#### Nested JSON & YAML file comparison:
[![asciicast](https://asciinema.org/a/lswyzmZLO04RRFVDOTzlK6nzo.svg)](https://asciinema.org/a/lswyzmZLO04RRFVDOTzlK6nzo)
#### Choosing the alternative output format
[![asciicast](https://asciinema.org/a/lqKv4iz8PbtDhS4sZBaxIPJmD.svg)](https://asciinema.org/a/lqKv4iz8PbtDhS4sZBaxIPJmD)
[![asciicast](https://asciinema.org/a/RNiVtfDofTBNge34yKe8NuBqn.svg)](https://asciinema.org/a/RNiVtfDofTBNge34yKe8NuBqn)
#### Importing the ___generate_diff___ function
[![asciicast](https://asciinema.org/a/7difl4pWNoQXk9wrlf3t1xQsz.svg)](https://asciinema.org/a/7difl4pWNoQXk9wrlf3t1xQsz)
