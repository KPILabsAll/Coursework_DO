import numpy as np


def hull_search(points: np.ndarray) -> np.ndarray:
    if (len(points) % 3) != 0:
        return ValueError('the number of points must be a multiple of 3')

    # sort points by x then by y
    points = np.array(sorted(points, key=lambda p: p[0]))

    result_triangles = []

    (largest_triangle, points_groups) = get_largest_triangle(points)
    result_triangles.append(largest_triangle)

    for points_group in points_groups:
        if len(points_group) > 0:
            result_triangles += hull_search(points_group)

    return result_triangles


# helper functions

def get_convex_hull(points: np.ndarray) -> np.ndarray:
    if len(points) < 3:
        return ValueError('at least 3 points required')

    link = lambda a, b: np.concatenate((a, b[1:]))

    def dome(sample, base):
        h, t = base
        dists = np.dot(sample - h, np.dot(((0, -1), (1, 0)), (t - h)))
        outer = np.repeat(sample, dists > 0, 0)
        edge = lambda a, b: np.concatenate(([a], [b]))

        if len(outer):
            pivot = sample[np.argmax(dists)]
            return link(dome(outer, edge(h, pivot)),
                        dome(outer, edge(pivot, t)))
        else:
            return base

    if len(points) > 2:
        axis = points[:, 0]
        base = np.take(points, [np.argmin(axis), np.argmax(axis)], 0)
        return link(dome(points, base),
                    dome(points, base[::-1]))
    else:
        return points


def can_build_triangle(a, b, c, points: np.ndarray) -> bool:
    (a_count, b_count, c_count) = (0, 0, 0)  # points that are separated by each triangle side
    triangle = np.array([a, b, c])
    for point in points:
        if (any(p[0] == point[0] and p[1] == point[1] for p in triangle)):
            continue

        if is_inside_convex_polygon(triangle, point):
            return False

        a_count += int(is_separated_by_side(triangle, 0, point))
        b_count += int(is_separated_by_side(triangle, 1, point))
        c_count += int(is_separated_by_side(triangle, 2, point))

    any_points_isolated = (a_count % 3 != 0 or b_count % 3 != 0 or c_count % 3 != 0)

    return not any_points_isolated


def get_triangle_area(a, b, c) -> float:
    area = 0.5 * abs((a[0] * (b[1] - c[1])) + (b[0] * (c[1] - a[1])) + (c[0] * (a[1] - b[1])))
    return area


def get_points_separated_by_triangle(triangle, points):
    result = [[], [], []]

    for p in points:
        if is_separated_by_side(triangle, 0, p):
            result[0].append(p)
        if is_separated_by_side(triangle, 1, p):
            result[1].append(p)
        if is_separated_by_side(triangle, 2, p):
            result[2].append(p)

    return result


def get_largest_triangle(points: np.ndarray):
    if len(points) == 3:
        return (points, [[], [], []])

    largest_triangle = None
    largest_triangle_area = 0

    hull = get_convex_hull(points)
    for a in hull:
        exclude_a = hull[(hull[:, 0] != a[0]) & (hull[:, 1] != a[1])]
        for b in exclude_a:
            exclude_ab_arr = exclude_a[(exclude_a[:, 0] != b[0]) & (exclude_a[:, 1] != b[1])]
            for c in exclude_ab_arr:
                area = get_triangle_area(a, b, c)
                if can_build_triangle(a, b, c, points) and area > largest_triangle_area:
                    largest_triangle = np.array([a, b, c])
                    largest_triangle_area = area

    separated_points = get_points_separated_by_triangle(largest_triangle, points)

    return (largest_triangle, separated_points)


def is_inside_convex_polygon(polygon, point) -> bool:
    sign = 0
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % 3]
        v1 = (p1[0] - point[0], p1[1] - point[1])
        v2 = (p2[0] - point[0], p2[1] - point[1])
        if sign == 0:
            sign = 1 if cross_product(v1, v2) > 0 else -1
        cross_sign = -1 if cross_product(v1, v2) < 0 else 1
        if cross_sign != sign:
            return False
    return True


def cross_product(p1, p2):
    (x1, y1) = (p1[0], p1[1])
    (x2, y2) = (p2[0], p2[1])
    return x1 * y2 - x2 * y1


def is_separated_by_side(triangle, side_index, point) -> bool:
    (a, b, c) = (triangle[(side_index + 1) % 3], triangle[(side_index + 2) % 3], triangle[side_index])
    vector_a = (a[0] - point[0], a[1] - point[1])
    vector_b = (b[0] - point[0], b[1] - point[1])
    vector_c = (c[0] - point[0], c[1] - point[1])
    return cross_product(vector_a, vector_c) * cross_product(vector_a, vector_b) > 0 \
           and cross_product(vector_b, vector_c) * cross_product(vector_b, vector_a) > 0
