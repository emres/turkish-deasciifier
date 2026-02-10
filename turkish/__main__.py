# -*- coding: utf-8 -*-
"""
CLI entry point for turkish-deasciify.

Example usage:
    $ echo "Opusmegi cagristiran catirtilar." | turkish-deasciify
    $ cat somefile.txt | turkish-deasciify
"""

import sys

from turkish.deasciifier import Deasciifier


def main() -> None:
    text = sys.stdin.read()
    deasciifier = Deasciifier(text)
    result = deasciifier.convert_to_turkish()
    sys.stdout.write(result)


if __name__ == "__main__":
    main()
