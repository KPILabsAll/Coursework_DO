from helpers import calculate_total_combination_area, add_triangles, parse_result


def print_results(triangle_combination, algorythm):
    triangle_combination = parse_result(triangle_combination, algorythm)
    print("--------------------------------------------")
    print("Results:")
    print("--------------------------------------------")
    print("Combination with Max Area:")
    print("--------------------------------------------")
    i = 0
    for triangle in triangle_combination:
        i += 1
        print('Triangle', f'{i}:', triangle)
    print("--------------------------------------------")
    print("Area:", calculate_total_combination_area(triangle_combination))
    add_triangles(triangle_combination)
