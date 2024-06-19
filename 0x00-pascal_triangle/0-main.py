#!/usr/bin/python3
"""
0-main
"""
generer_triangle_pascal = __import__('0-pascal_triangle').generer_triangle_pascal

def afficher_triangle(triangle):
    """
    Afficher le triangle
    """
    for ligne in triangle:
        print("[{}]".format(",".join([str(element) for element in ligne])))


if __name__ == "__main__":
    afficher_triangle(generer_triangle_pascal(5))
