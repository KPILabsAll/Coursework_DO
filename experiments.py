import time
from matplotlib import pyplot as plt
from brute_force import brute_force
from graph_state_search import graph_state_search
from hull_search import hull_search
from helpers import random_points_generator, \
    calculate_total_combination_area, \
    parse_result
from algorythm_enum import AlgorithmEnum


def triangles_quantity_to_time_experiment():
    n = 2
    print("--------------------------------------------")
    print("Input data for your experiment: ")
    print("--------------------------------------------")

    triangles = int(input("Enter N (number of triangles): "))
    print("--------------------------------------------")

    experiments = int(input("Enter the number of experiments: "))
    print("--------------------------------------------")

    mu = 0.5
    sigma = mu * 0.5

    quantity = []
    average_time_graph_state_search_list = []
    average_time_hull_search_list = []
    average_time_brute_force_list = []

    for i in range(n, triangles + 1):
        quantity.append(i)

        average_time_graph_state_search = 0
        average_time_hull_search = 0
        average_time_brute_force = 0

        for j in range(1, experiments + 1):
            points = random_points_generator(i, mu, sigma)
            results_list = solving_problem_time(points)
            average_time_graph_state_search += results_list[0]
            average_time_hull_search += results_list[1]
            average_time_brute_force += results_list[2]

        average_time_graph_state_search_list.append(average_time_graph_state_search / experiments)
        average_time_hull_search_list.append(average_time_hull_search / experiments)
        average_time_brute_force_list.append(average_time_brute_force / experiments)

    plt.plot(quantity, average_time_graph_state_search_list, marker='o', label='Graph State Search')
    plt.plot(quantity, average_time_hull_search_list, marker='o', label='Hull Search')
    plt.plot(quantity, average_time_brute_force_list, marker='o', label='Brute Force')
    plt.xlabel('Quantity of the Triangles')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Quantity to Time')
    plt.legend()
    plt.grid(True)
    plt.show()


def triangles_quantity_to_accuracy_experiment():
    n = 2
    print("--------------------------------------------")
    print("Input data for your experiment: ")
    print("--------------------------------------------")

    triangles = int(input("Enter N (number of triangles): "))
    print("--------------------------------------------")

    experiments = int(input("Enter the number of experiments: "))
    print("--------------------------------------------")

    mu = 0.5
    sigma = mu * 0.5

    quantity = []
    average_shift_graph_state_search_list = []
    average_shift_hull_search_list = []
    average_shift_brute_force_list = []

    for i in range(n, triangles + 1):
        quantity.append(i)

        average_shift_graph_state_search = 0
        average_shift_hull_search = 0
        average_shift_brute_force = 0

        for j in range(1, experiments + 1):
            points = random_points_generator(i, mu, sigma)
            results_list = solving_problem_shift(points)
            average_shift_graph_state_search += results_list[0]
            average_shift_hull_search += results_list[1]
            average_shift_brute_force += results_list[2]

        average_shift_graph_state_search_list.append(average_shift_graph_state_search / experiments)
        average_shift_hull_search_list.append(average_shift_hull_search / experiments)
        average_shift_brute_force_list.append(average_shift_brute_force / experiments)

    plt.plot(quantity, average_shift_graph_state_search_list, marker='o', label='Graph State Search')
    plt.plot(quantity, average_shift_hull_search_list, marker='o', label='Hull Search')
    plt.plot(quantity, average_shift_brute_force_list, marker='o', label='Brute Force')
    plt.xlabel('Quantity of the Triangles')
    plt.ylabel('Average Shift')
    plt.title('Quantity to Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()


def parameters_to_accuracy_experiment():
    print("--------------------------------------------")
    print("Input data for your experiment: ")
    print("--------------------------------------------")
    n = int(input("Enter N (number of triangles): "))
    print("--------------------------------------------")

    mu = float(input("Enter mu: "))
    print("--------------------------------------------")

    sigm = float(input("Enter number of changes of sigma: "))
    print("--------------------------------------------")

    experiments = int(input("Enter the number of experiments: "))
    print("--------------------------------------------")

    delta_sigma = 1 / sigm

    quantity = []
    average_shift_graph_state_search_list = []
    average_shift_hull_search_list = []
    average_shift_brute_force_list = []

    r = 0
    current_sigma = 0

    while r < sigm:
        current_sigma += delta_sigma

        quantity.append(current_sigma)

        average_shift_graph_state_search = 0
        average_shift_hull_search = 0
        average_shift_brute_force = 0

        for j in range(1, experiments + 1):
            points = random_points_generator(n, mu, current_sigma)
            results_list = solving_problem_shift(points)
            average_shift_graph_state_search += results_list[0]
            average_shift_hull_search += results_list[1]
            average_shift_brute_force += results_list[2]

        average_shift_graph_state_search_list.append(average_shift_graph_state_search / experiments)
        average_shift_hull_search_list.append(average_shift_hull_search / experiments)
        average_shift_brute_force_list.append(average_shift_brute_force / experiments)

        r += 1

    plt.plot(quantity, average_shift_graph_state_search_list, marker='o', label='Graph State Search')
    plt.plot(quantity, average_shift_hull_search_list, marker='o', label='Hull Search')
    plt.plot(quantity, average_shift_brute_force_list, marker='o', label='Brute Force')
    plt.xlabel('Dispersion for distribution')
    plt.ylabel('Average Shift')
    plt.title('Dispersion vs Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()


def solving_problem_time(points):
    # Graph State Search Algorithm
    start_time_graph_state_search = time.time()

    graph_state_search(points, [])

    end_time_graph_state_search = time.time()
    elapsed_time_graph_state_search = end_time_graph_state_search - start_time_graph_state_search

    # Hull Search Algorithm
    start_time_hull_search = time.time()

    hull_search(points)

    end_time_hull_search = time.time()
    elapsed_time_hull_search = end_time_hull_search - start_time_hull_search

    # Brute Force Algorithm
    start_time_brute_force = time.time()

    brute_force(points)

    end_time_brute_force = time.time()
    elapsed_time_brute_force = end_time_brute_force - start_time_brute_force

    return [elapsed_time_graph_state_search, elapsed_time_hull_search, elapsed_time_brute_force]


def solving_problem_shift(points):
    # Graph State Search Algorithm
    graph_state_search_area = calculate_total_combination_area(
        parse_result(graph_state_search(points, []).triangles, AlgorithmEnum.graph_state_search))

    # Hull Search Algorithm
    hull_search_area = calculate_total_combination_area(
        parse_result(hull_search(points), AlgorithmEnum.hull_search))

    # Brute Force Algorithm
    brute_force_area = calculate_total_combination_area(brute_force(points))

    return [abs(graph_state_search_area - brute_force_area), abs(hull_search_area - brute_force_area), 0]
