from helpers import calculate_total_combination_area, add_triangles
from algorythm_enum import AlgorithmEnum


def print_results(triangle_combination):
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


def print_experiment_matrix(average_graph_state_search_list,
                            average_hull_search_list,
                            average_brute_force_list,
                            quantity):
    algs = ["Graph State Search", "Hull Search", "Brute Force"]
    column_numbers = quantity
    alg_values = [average_graph_state_search_list, average_hull_search_list, average_brute_force_list]

    max_alg_name_length = max(len(name) for name in algs)

    print(f"{'':<{max_alg_name_length + 2}}", end="")
    for number in column_numbers:
        print(f"{number:<10.5f}", end="")
    print()

    for i, algorithm in enumerate(alg_values):
        print(f"{algs[i]:<{max_alg_name_length}}", end="  ")
        for value in algorithm:
            print(f"{value:<10.5f}", end="")
        print()


