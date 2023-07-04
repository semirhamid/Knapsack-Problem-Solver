import argparse
from ga import genetic_algorithm
from sa import simulated_annealing
from ha import hill_climbing

# Define command-line arguments
parser = argparse.ArgumentParser(description='Solve the knapsack problem using various algorithms.')
parser.add_argument('--algorithm', type=str, choices=['ga', 'sa', 'ha'], required=True,
                    help='the algorithm to use (genetic algorithm, simulated annealing, or hill climbing)')
parser.add_argument('--file', type=str, required=True,
                    help='the input file containing the knapsack problem data')
parser.add_argument('--population_size', type=int, default=100,
                    help='the size of the population for the genetic algorithm (default: 100)')
parser.add_argument('--num_generations', type=int, default=50,
                    help='the size of the population for the genetic algorithm (default: 100)')
parser.add_argument('--mutation_rate', type=float, default=0.01,
                    help='the mutation rate for the genetic algorithm (default: 0.01)')
parser.add_argument('--temperature', type=float, default=1000,
                    help='the initial temperature for simulated annealing (default: 1000)')
parser.add_argument('--cooling_rate', type=float, default=0.5,
                    help='the cooling rate for simulated annealing (default: 0.5)')

# Parse command-line arguments
args = parser.parse_args()

# Read input file
with open(args.file, 'r') as f:
    capacity = int(f.readline())
    f.readline()
    num_items, values, weights = [], [], []
    for line in f.readlines():
        weights.append(float(line.split(',')[1]))
        values.append(int(line.split(',')[2]))
        num_items.append(int(line.split(',')[3]))

# Call the appropriate algorithm function based on the selected algorithm
if args.algorithm == 'ga':
    best_solution = genetic_algorithm(capacity, values, num_items, weights, args.population_size, args.num_generations, args.mutation_rate)
elif args.algorithm == 'sa':
    best_solution = simulated_annealing(values, weights, num_items, capacity, args.temperature, args.cooling_rate)
else:
    best_solution = hill_climbing(values, weights, capacity, num_items)

# Print the best solution found
print('Best solution found:', best_solution)

# sample Command
# python knapsack.py --algorithm ga --file test1.txt --population_size 200 --mutation_rate 0.05
