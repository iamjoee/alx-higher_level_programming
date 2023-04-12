#!/usr/bin/python3
"""this defines the Pascal's Triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size j
    Returns a list of lists of integers representing the triangle
    """
    if j <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != j:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
