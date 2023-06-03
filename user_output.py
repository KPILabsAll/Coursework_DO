from helpers import calculate_total_combination_area, add_triangles, parse_result
from algorythm_enum import AlgorithmEnum


def print_results(triangle_combination, algorythm):
    triangle_combination = parse_result(triangle_combination, algorythm)
    res = ""
    res += "--------------------------------------------\n"
    res += "Results:\n"
    res += "--------------------------------------------\n"
    res += "Combination with Max Area:\n"
    res += "--------------------------------------------\n"
    i = 0
    for triangle in triangle_combination:
        i += 1
        res += f'Triangle {i}: {triangle}\n'
    res += "--------------------------------------------\n"
    res += f"Area: {calculate_total_combination_area(triangle_combination)}"

    print(res)
    add_triangles(triangle_combination)

    return res


def print_results_to_file(results, algorythm: AlgorithmEnum):
    filename = f"Results {algorythm.name}.txt"

    with open(filename, 'w') as file:
        file.write(results)
