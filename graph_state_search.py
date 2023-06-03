import itertools


class SearchResult:
    def __init__(self, triangles, total_area):
        self.triangles = triangles
        self.max_total_area = total_area


def graph_state_search(points) -> SearchResult:
    points = sorted(points, key=lambda p: p[0])
    return graph_state_search_rec(points, [])


def graph_state_search_rec(points, existing_triangles) -> SearchResult:
    if len(points) % 3 != 0:
        return ValueError('the number of points must be a multiple of 3')

    if len(points) == 3:
        if (not can_build_triangle(points, points, existing_triangles)):
            return SearchResult([], 0)
        area = get_triangle_area(points)
        return SearchResult([points], area)

    triangles = get_triangles_combinations(points)
    max_area_triangles = None
    max_total_area = 0

    for t in triangles:
        if (can_build_triangle(t, points, existing_triangles)):
            remaining_points = [p for p in points if tuple(p) not in set([tuple(p1) for p1 in t])]
            res = graph_state_search_rec(remaining_points, existing_triangles + [t])
            if (res.max_total_area == 0):
                continue

            res.max_total_area += get_triangle_area(t)
            res.triangles.append(t)
            if (res.max_total_area > max_total_area):
                max_area_triangles = res.triangles
                max_total_area = res.max_total_area

    return SearchResult(max_area_triangles, max_total_area)


# helper functions
def get_triangle_area(points) -> float:
    (a, b, c) = (points[0], points[1], points[2])
    area = 0.5 * abs((a[0] * (b[1] - c[1])) + (b[0] * (c[1] - a[1])) + (c[0] * (a[1] - b[1])))
    return area


def cross_product(p1, p2):
    (x1, y1) = (p1[0], p1[1])
    (x2, y2) = (p2[0], p2[1])
    return x1 * y2 - x2 * y1


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


def triangles_intersect(t1, t2) -> bool:
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    def segments_intersect(s1, s2):
        A, B = s1[0], s1[1]
        C, D = s2[0], s2[1]
        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

    def get_sides(polygon):
        last_point = polygon[-1]
        for point in polygon:
            yield (last_point, point)
            last_point = point

    return any(segments_intersect(side1, side2)
               for side1, side2 in itertools.product(get_sides(t1), get_sides(t2)))


def get_triangle_area(points) -> float:
    (a, b, c) = (points[0], points[1], points[2])
    area = 0.5 * abs((a[0] * (b[1] - c[1])) + (b[0] * (c[1] - a[1])) + (c[0] * (a[1] - b[1])))
    return area


def can_build_triangle(t, points, existing_triangles) -> bool:
    for t_i in existing_triangles:
        if triangles_intersect(t, t_i):
            return False

    for point in points:
        if (any(p[0] == point[0] and p[1] == point[1] for p in t)):
            continue
        if is_inside_convex_polygon(t, point):
            return False

    return True


def get_triangles_combinations(points):
    pivot_point = points[0]
    size = len(points) - 2
    res = []
    for j in range(size):
        for i in range(j + 1):
            res.append([pivot_point, points[i + 1], points[j + 2]])

    return res
