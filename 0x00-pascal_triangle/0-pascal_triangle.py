#!/usr/bin/python3
"""
0-triangle_pascal
"""

def generer_triangle_pascal(taille):
    """
    Renvoie une liste d'entiers
    représentant le triangle de Pascal de taille 'taille'
    renvoie une liste vide si taille <= 0
    """
    triangle = []
    if taille <= 0:
        return triangle
    triangle = [[1]]
    for i in range(1, taille):
        ligne = [1]
        for j in range(len(triangle[i - 1]) - 1):
            ligne.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        ligne.append(1)
        triangle.append(ligne)
    return triangle
