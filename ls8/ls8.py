#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

# if len (sys.argv) !=2:
#         print("usage: cpu.py filename")
#         sys.exit(1)

# filename = sys.argv[1]

cpu = CPU()

cpu.load()
cpu.run()