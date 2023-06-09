import csv
from helpers import random_points_generator


def user_input():
    print("\n--------------------------------------------")
    print("Choose data source:")
    print("1. Generate random data")
    print("2. Import data from file")
    print("3. Enter data manually")
    print("--------------------------------------------")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        return generate_random_points()
    elif choice == '2':
        return input_file()
    elif choice == '3':
        return input_points()
    else:
        print("Invalid choice!")
        return None


def generate_random_points():
    print("--------------------------------------------")
    n = int(input("Enter the quantity of triangles (n): "))
    print("--------------------------------------------")
    mu = float(input("Enter mu (average value for generation): "))
    print("--------------------------------------------")
    sigma = float(input("Enter sigma (dispersion for values): "))
    print("--------------------------------------------")
    return random_points_generator(n, mu, sigma)


def input_file():
    print("--------------------------------------------")
    filename = input("Enter the filename with your data: ")
    print("--------------------------------------------")
    points = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            points.append((float(row[0]), float(row[1])))

    if (len(points) % 3) != 0:
        return ValueError('the number of points must be a multiple of 3')

    formatted_points = [points[1], points[0]] + points[2:]
    return formatted_points


def input_points():
    print("--------------------------------------------")
    n = int(input("Enter the quantity of triangles (n): "))
    print("--------------------------------------------")

    points = []
    for i in range(3 * n):
        x = float(input(f"Enter x-coordinate of point {i + 1}: "))
        y = float(input(f"Enter y-coordinate of point {i + 1}: "))
        points.append((x, y))

    return points
