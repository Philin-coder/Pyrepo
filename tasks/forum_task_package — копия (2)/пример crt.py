# -*- coding: utf-8 -*-

import random
import msvcrt

while True:
    slots = [random.randint(1, 5) for _ in range(3)]
    print("-" * 13)
    print("| {} | {} | {} |".format(*slots))
    print("-" * 13)
    if slots[0] == slots[1] == slots[2]:
        print("WINNED")
    else:
        print("LOSED")
    print("Press Esc for exit, or any key to continue.")
    if msvcrt.getch() == b"\x1b":
        break
