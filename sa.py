import random
import math

def evaluation_function(values, weights, capacity, solution):
    # Compute the total value and weight of the solution
    total_value = 0
    total_weight = 0
    for i in range(len(values)):
        total_value += values[i] * solution[i]
        total_weight += weights[i] * solution[i]

    # If the weight exceeds the capacity or the number of items exceeds the limit,
    # the solution is invalid and has no value
    if total_weight > capacity:
        return total_weight, -1

    return total_weight, total_value

def acceptance_probability(current_fitness, neighbor_fitness, temperature):
    if neighbor_fitness > current_fitness:
        return 1.0
    else:
        diff = neighbor_fitness - current_fitness
        return math.exp(diff / temperature)

def simulated_annealing(values, weights, num_items, capacity, temperature, cooling_rate):
    # Start with a random initial solution
    total_weight = 0
    current_solution = [0]*len(values)
    for i in range(len(num_items)):
        rand = random.randint(0, num_items[i])
        if total_weight+rand*weights[i] <= capacity:
            total_weight += rand * weights[i]
            current_solution[i] = rand
    _, current_value = evaluation_function(values, weights, capacity, current_solution)

    # Set the initial best solution to the current solution
    best_solution = current_solution.copy()
    best_value = current_value
    while True:
        # Choose the random neighbor that satisfies the capacity and number of items constraint
        while True:
            neighbor_solution = current_solution.copy()
            i = random.randint(0, len(neighbor_solution)-1)
            neighbor_solution[i] = random.randint(0, num_items[i])
            neighbor_weight, neighbor_value = evaluation_function(values, weights, capacity, neighbor_solution)
            if neighbor_weight <= capacity: break
        
        if random.random() < acceptance_probability(current_value, neighbor_value, temperature):
            current_solution = neighbor_solution.copy()
            current_value = neighbor_value
        
        if current_value > best_value:
            best_solution = current_solution.copy()
            best_value = current_value
        
        temperature *= cooling_rate
        if temperature <= 0: break
    return best_solution, best_value

if __name__ == '__main__':
    # Example usage
    values = [10, 20, 15, 8, 25, 12, 18, 14, 30, 22]
    weights = [5, 10, 7, 4, 12, 6, 9, 8, 15, 10]
    max_weight = 50
    available_items = [5, 8, 4, 6, 7, 3, 9, 5, 10, 6]
    print(simulated_annealing(values, weights, available_items, max_weight, 100, 0.5))