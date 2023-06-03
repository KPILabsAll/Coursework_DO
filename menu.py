from user_input import user_input
from user_output import print_results, print_results_to_file
from brute_force import brute_force
from graph_state_search import graph_state_search
from hull_search import hull_search
from algorythm_enum import AlgorithmEnum
from experiments import triangles_quantity_to_time_experiment, \
    triangles_quantity_to_accuracy_experiment, \
    parameters_to_accuracy_experiment


def menu():
    while True:
        print("--------------------------------------------")
        print("Menu:")
        print("1. Solve problem")
        print("2. Start experiment")
        print("3. Exit")
        print("--------------------------------------------")
        choice = input("Enter your choice (1-3): ")
        print("\n")

        if choice == '1':
            solve_problem()
        elif choice == '2':
            choose_experiment()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")


def solve_problem():
    print("--------------------------------------------")
    print("Choose an algorithm:")
    print("1. Graph State Search Algorithm")
    print("2. Hull Search Algorithm")
    print("3. Brute Force Algorithm")
    print("--------------------------------------------")
    choice = input("Enter your choice (1-3): ")

    data = user_input()
    print("Points: ", data)

    if choice == '1':
        print_results_to_file(
            print_results(graph_state_search(data).triangles, AlgorithmEnum.graph_state_search),
            AlgorithmEnum.graph_state_search
        )
    elif choice == '2':
        print_results_to_file(
            print_results(hull_search(data), AlgorithmEnum.hull_search),
            AlgorithmEnum.hull_search
        )
    elif choice == '3':
        print_results_to_file(
            print_results(brute_force(data), AlgorithmEnum.brute_force),
            AlgorithmEnum.brute_force
        )
    else:
        print("Invalid choice!")


def choose_experiment():
    print("--------------------------------------------")
    print("Choose an experiment:")
    print("1. The effect of the number of triangles on the algorithm's running time")
    print("2. The effect of the number of triangles on the accuracy of algorithms")
    print("3. The effect of the parameters of the problem on the accuracy of algorithms")
    print("--------------------------------------------")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        triangles_quantity_to_time_experiment()
    elif choice == '2':
        triangles_quantity_to_accuracy_experiment()
    elif choice == '3':
        parameters_to_accuracy_experiment()
    else:
        print("Invalid choice!")


def main():
    try:
        menu()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
