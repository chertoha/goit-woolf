import random
import math


def sphere_function(x):
    return sum(xi ** 2 for xi in x)


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    current_value = func(current)
    step_size = 0.1

    for _ in range(iterations):
        neighbor = [current[i] +
                    random.uniform(-step_size, step_size) for i in range(dim)]
        neighbor = [max(bounds[i][0], min(bounds[i][1], neighbor[i]))
                    for i in range(dim)]
        neighbor_value = func(neighbor)

        if abs(neighbor_value - current_value) < epsilon and all(abs(neighbor[i] - current[i]) < epsilon for i in range(dim)):
            break

        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value

    return current, current_value


def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    best = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    best_value = func(best)

    for _ in range(iterations):
        candidate = [random.uniform(bounds[i][0], bounds[i][1])
                     for i in range(dim)]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best, best_value = candidate, candidate_value

        if abs(candidate_value - best_value) < epsilon:
            break

    return best, best_value


def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    dim = len(bounds)
    current = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    current_value = func(current)

    for _ in range(iterations):
        temp *= cooling_rate
        if temp < epsilon:
            break

        neighbor = [current[i] + random.uniform(-0.1, 0.1) for i in range(dim)]
        neighbor = [max(bounds[i][0], min(bounds[i][1], neighbor[i]))
                    for i in range(dim)]
        neighbor_value = func(neighbor)

        delta = neighbor_value - current_value
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_value = neighbor, neighbor_value

    return current, current_value


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
