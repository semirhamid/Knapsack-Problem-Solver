import random

def generate_individual(capacity, num_items, weights):
    n = len(num_items)
    total_weight = 0
    current_solution = [0]*n
    for i in range(n):
        rand = random.randint(0, num_items[i])
        if total_weight+rand*weights[i] <= capacity:
            total_weight += rand * weights[i]
            current_solution[i] = rand
    return current_solution

def generate_population(capacity, num_items, weights, population_size):
    return [generate_individual(capacity, num_items, weights) for _ in range(population_size)]

def evaluate_fitness(individual, values, weights, capacity):
    total_value = 0
    total_weight = 0
    for i in range(len(individual)):
        if individual[i] > 0:
            total_value += values[i] * individual[i]
            total_weight += weights[i] * individual[i]
    if total_weight > capacity:
        return 0  # Penalize solutions that exceed the maximum weight
    else:
        return total_value

def selection(population, values, weights, capacity, population_size):
    population.sort(key= lambda i: evaluate_fitness(i, values, weights, capacity), reverse = True)
    return population[:population_size]

def crossover(parent1, parent2):
    child1 = [0] * len(parent1)
    child2 = [0] * len(parent2)
    for i in range(len(parent1)):
        if parent1[i] > 0 or parent2[i] > 0:
            child1[i] = random.choice([parent1[i], parent2[i]])
            child2[i] = random.choice([parent1[i], parent2[i]])
    return child1, child2

def mutate(individual, mutation_rate, available_items):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, min(1, available_items[i]))  # Update the selected quantity
    return individual

def genetic_algorithm(capacity, values, num_items, weights, population_size, num_generations, mutation_rate):
    population = generate_population(capacity, num_items, weights, population_size)

    for generation in range(num_generations):
        population = selection(population, values, weights, capacity, population_size)
        next_generation = []

        for _ in range(population_size // 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)

            child1, child2 = crossover(parent1, parent2)

            child1 = mutate(child1, mutation_rate, num_items)
            child2 = mutate(child2, mutation_rate, num_items)

            next_generation.extend([child1, child2])

        population += next_generation

    best_individual = max(population, key=lambda i: evaluate_fitness(i, values, weights, capacity))
    best_fitness = evaluate_fitness(best_individual, values, weights, capacity)

    return best_individual, best_fitness

if __name__ == '__main__':
    # Knapsack problem parameters
    values = [10, 20, 15, 8, 25, 12, 18, 14, 30, 22]
    weights = [5, 10, 7, 4, 12, 6, 9, 8, 15, 10]
    max_weight = 50
    available_items = [5, 8, 4, 6, 7, 3, 9, 5, 10, 6]  # Number of available items for each type

    # Genetic algorithm parameters
    population_size = 50
    mutation_rate = 0.01
    num_generations = 10

    pop = generate_population(max_weight, available_items, weights, population_size)
    best_solution, best_fitness = genetic_algorithm(max_weight, values, available_items, weights, population_size, num_generations, mutation_rate)

    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)