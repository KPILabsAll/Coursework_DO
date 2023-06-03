import random
from matplotlib import pyplot as plt
from algorythm_enum import AlgorithmEnum


def random_points_generator(n, mu, sigma):
    points = []

    for _ in range(3 * n):
        x = random.gauss(mu, sigma)
        y = random.gauss(mu, sigma)
        points.append((x, y))

    return points


def add_triangles(triangles):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for triangle in triangles:
        ax.add_patch(plt.Polygon(triangle, fill=False))

    ax.autoscale()
    plt.show()


def parse_result(triangle_combinations, algorythm: AlgorithmEnum):
    formatted_result = triangle_combinations
    if algorythm.value == AlgorithmEnum.hull_search.value:
        formatted_result = tuple(tuple(map(tuple, arr.tolist())) for arr in triangle_combinations)

    return formatted_result


def calculate_triangle_area(triangle):
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]

    area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    return area


def calculate_total_combination_area(triangle_combination):
    return sum(calculate_triangle_area(triangle) for triangle in triangle_combination)
