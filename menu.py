from user_input import user_input
from user_output import print_results
from brute_force import brute_force
from graph_state_search import graph_state_search
from hull_search import hull_search
from algorythm_enum import AlgorithmEnum


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

        # elif choice == '2':
        #     choose_experiment()
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

    if choice == '1':
        print_results(graph_state_search(data, []).triangles, AlgorithmEnum.graph_state_search)
    elif choice == '2':
        print_results(hull_search(data), AlgorithmEnum.hull_search)
    elif choice == '3':
        print_results(brute_force(data), AlgorithmEnum.brute_force)
    else:
        print("Invalid choice!")


def main():
    try:
        menu()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
