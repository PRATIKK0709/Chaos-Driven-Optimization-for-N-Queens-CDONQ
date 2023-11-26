import random
import numpy as np

def initialize_population(n, population_size):
    return [[random.randint(0, n - 1) for _ in range(n)] for _ in range(population_size)]

def calculate_fitness(board):
    n = len(board)
    clashes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                clashes += 1
    return n - clashes

def chaos_perturbation(board, chaos_coefficient):
    n = len(board)
    perturbed_board = [0] * n

    for i in range(n):
        perturbation = chaos_coefficient * random.uniform(-1, 1)
        perturbed_board[i] = (board[i] + perturbation) % n

    return perturbed_board

def chaos_driven_optimization_n_queens(n, population_size=100, generations=1000, chaos_coefficient=0.1):
    population = initialize_population(n, population_size)

    for generation in range(generations):
        # Apply chaos-driven perturbation to the population
        perturbed_population = [chaos_perturbation(ind, chaos_coefficient) for ind in population]

        #Evaluate fitness
        fitness_values = [calculate_fitness(ind) for ind in perturbed_population]
        sum_fitness = sum(fitness_values)
        if sum_fitness == 0:
            probabilities = np.ones(population_size) / population_size
        else:
            probabilities = np.array(fitness_values) / sum_fitness
            probabilities /= probabilities.sum()


    # Return the best solution found
    best_solution = max(perturbed_population, key=lambda x: calculate_fitness(x))
    return best_solution

# Example usage for N = 8
n = 8
solution = chaos_driven_optimization_n_queens(n)
print("Final Solution:")
print(solution)
