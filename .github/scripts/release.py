#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from importlib.metadata import version


def entry_point() -> None:
    parser = ArgumentParser()
    parser.add_argument("-v", "--version", action="store_true")

    args = parser.parse_args()

    if args.version:
        print(version("dataclass_codec"))
        sys.exit()
