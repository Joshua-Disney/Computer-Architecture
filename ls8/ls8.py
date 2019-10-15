#!/usr/bin/env python3

"""Main."""

# call.ls8 caches the next instruction, goes to new address and executes first instruction
# interrupts.ls8
# keyboard.ls8
# mult.ls8
# print8.ls8
# printstr.ls8
# sctest.ls8
# stack.ls8
# stackoverflow.ls8

import sys
from cpu import *

cpu = CPU()

cpu.load()
cpu.run()