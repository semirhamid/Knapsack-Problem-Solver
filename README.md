# Knapsack Problem Solver 🎒

Welcome to the Knapsack Problem Solver! This is a Python implementation for solving the classic Knapsack problem using various algorithms.

## About the Knapsack Problem

The Knapsack problem is a classic optimization problem in computer science and combinatorial optimization. It is often described as follows:

Given a set of items, each with a weight and a value, determine the number of each item to include in a knapsack so that the total weight is less than or equal to a given limit and the total value is maximized.

## Features

- Implementation of various algorithms to solve the Knapsack problem, including:
  - Brute force
  - Dynamic programming
  - Greedy algorithm
  - Branch and bound
- Support for both 0/1 Knapsack (where each item can be either included or excluded) and Fractional Knapsack (where items can be divided)
- Customizable input for adding items with different weights and values
- Detailed explanation and comments in the code for better understanding

## Algorithms

### Brute Force
This algorithm tries all possible combinations of items and selects the one with the maximum value that satisfies the weight constraint.

### Dynamic Programming
Dynamic programming is used to solve the problem by breaking it down into smaller subproblems and solving them iteratively.

### Greedy Algorithm
The greedy algorithm selects items based on their value-to-weight ratio, choosing the item with the highest ratio first.

### Branch and Bound
Branch and bound is a more efficient version of the brute force approach, where branches that cannot lead to a better solution are pruned.

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/knapsack-problem-solver.git
   ```
2. Navigate into the project directory:
   ```sh
   cd knapsack-problem-solver
   ```
3. Run the Python script:
   ```sh
   python knapsack_solver.py
   ```

## Contributing

Contributions to the Knapsack Problem Solver project are welcome! If you have suggestions, improvements, or want to add new features, feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support regarding the Knapsack Problem Solver, you can reach out to the project maintainer:
