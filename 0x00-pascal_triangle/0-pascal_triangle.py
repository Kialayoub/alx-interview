#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    """
    tab = []
    if n <= 0:
        return tab
    tab = [[1]]
    for i in range(1, n):
        t = [1]
        for j in range(len(tab[i - 1]) - 1):
            curr = tab[i - 1]
            t.append(tab[i - 1][j] + tab[i - 1][j + 1])
        t.append(1)
        tab.append(t)
    return tab
