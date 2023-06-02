from itertools import combinations


def brute_force(points):
    triangle_combinations = generate_point_triples(points)

    triangle_combinations_with_area = []
    for combination in triangle_combinations:
        total_area = sum(calculate_triangle_area(triangle) for triangle in combination)
        triangle_combinations_with_area.append((combination, total_area))

    max_area = max(triangle_combinations_with_area, key=lambda x: x[1])[1]

    for combination, area in triangle_combinations_with_area:
        if area == max_area:
            return combination


# helper functions

def generate_point_triples(points):
    triples = []
    n = len(points)

    for triple in combinations(points, 3):
        if can_form_triangle(triple):
            triples.append(triple)

    combinations_with_others = combinations(triples, len(points) // 3)

    valid_combinations = []
    for combination in combinations_with_others:
        intersect = False
        for i in range(len(combination)):
            for j in range(i + 1, len(combination)):
                if check_intersection(combination[i], combination[j]):
                    intersect = True
                    break
            if intersect:
                break
        if not intersect:
            valid_combinations.append(combination)

    return valid_combinations


def can_form_triangle(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)

    if a + b > c and b + c > a and c + a > b:
        return not are_collinear(points)

    return False


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def are_collinear(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def check_intersection(triangle1, triangle2):
    for i in range(3):
        segment1 = (triangle1[i], triangle1[(i + 1) % 3])
        for j in range(3):
            segment2 = (triangle2[j], triangle2[(j + 1) % 3])
            if segments_intersect(segment1, segment2):
                return True
    return False


def segments_intersect(segment1, segment2):
    p1, q1 = segment1
    p2, q2 = segment2
    if orientation(p1, q1, p2) != orientation(p1, q1, q2) and orientation(p2, q2, p1) != orientation(p2, q2, q1):
        return True
    return False


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def calculate_triangle_area(triangle):
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]

    area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    return area
