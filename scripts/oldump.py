#!/usr/bin/env python

import sys

import _init_path  # noqa: F401


if __name__ == "__main__":
    print("{}: Python {}.{}.{}".format(__file__, *sys.version_info), file=sys.stderr)

    from openlibrary.data import dump

    dump.main(sys.argv[1], sys.argv[2:])
