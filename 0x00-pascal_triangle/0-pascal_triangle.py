#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """
    Returns a list of integers
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        tmp = [1]
        for i in range(len(k[i - 1]) - 1):
            c = k[i - 1]
            tmp.append(k[i - 1][i] + k[i - 1][i + 1])
        tmp.append(1)
        k.append(tmp)
    return k
