#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for k in range(1, len(boxes) - 1):
        c = False
        for idx in range(len(boxes)):
            c = (k in boxes[idx] and k != idx)
            if c:
                break
        if c is False:
            return c
    return True
