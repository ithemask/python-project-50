#!/usr/bin/env python3
from gendiff.arg_parser import parse_args
from gendiff.gendiff import generate_diff


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
