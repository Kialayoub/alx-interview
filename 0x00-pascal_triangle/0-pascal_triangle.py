#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    tab = []
    if n <= 0:
        return tab
    tab = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(tab[i - 1]) - 1):
            curr = tab[i - 1]
            temp.append(tab[i - 1][j] + tab[i - 1][j + 1])
        temp.append(1)
        tab.append(temp)
    return tab
