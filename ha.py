import random

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

def select_neighbor(current_solution, values, weights, num_items, capacity):
    n = len(current_solution)
    current_weight, _ = evaluation_function(values, weights, capacity, current_solution)
    rem_weight = capacity - current_weight
    
    neighbors = []
    for i in range(n):
        # print(rem_weight+weights[i])
        for j in range(n):
            if rem_weight >= weights[j] and current_solution[j] < num_items[j]:
                neighbor = current_solution.copy()
                neighbor[j] += min(num_items[j]-current_solution[j], rem_weight//weights[j])
                neighbors.append(neighbor)
            
            if i!=j and current_solution[i]>0 and rem_weight+weights[i] >= weights[j] and current_solution[j] < num_items[j]:
                neighbor = current_solution.copy()
                neighbor[i] -= 1
                neighbor[j] += min(num_items[j]-neighbor[j], (rem_weight+weights[i])//weights[j])
                neighbors.append(neighbor)
                
    next_best = [0]*n
    next_best_val = 0
    for neighbor in neighbors:
        _, neighbor_val = evaluation_function(values, weights, capacity, neighbor)
        if neighbor_val > next_best_val:
            next_best_val = neighbor_val
            next_best = neighbor
    return next_best

def hill_climbing(values, weights, capacity, num_items):
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
        # Choose the best neighbor that satisfies the capacity and number of items constraint
        current_solution = select_neighbor(current_solution, values, weights, num_items, capacity)
        _, neighbor_value = evaluation_function(values, weights, capacity, current_solution)
        if neighbor_value > best_value:
            best_solution = current_solution
            best_value = neighbor_value
        else: break
    return best_solution, best_value


if __name__ == '__main__':
    # Example usage
    values = [10, 20, 15, 8, 25, 12, 18, 14, 30, 22]
    weights = [5, 10, 7, 4, 12, 6, 9, 8, 15, 10]
    max_weight = 50
    available_items = [5, 8, 4, 6, 7, 3, 9, 5, 10, 6]
    print(hill_climbing(values, weights, max_weight, available_items))