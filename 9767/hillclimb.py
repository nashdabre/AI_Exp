import random


def hill_climbing(problem):
    current_solution = problem.random_solution()
    while True:
        neighbors = problem.get_neighbors(current_solution)
        best_neighbor = max(neighbors, key=lambda neighbor: problem.heuristic(neighbor))
        if problem.heuristic(best_neighbor) <= problem.heuristic(current_solution):
            return current_solution
        current_solution = best_neighbor


class Problem:
    def __init__(self):
        pass

    def random_solution(self):
        pass

    def get_neighbors(self, solution):
        pass

    def heuristic(self, solution):
        pass


# Example usage:
class ExampleProblem(Problem):
    def __init__(self):
        super().__init__()
        self.solution = [random.randint(0, 100) for _ in range(5)]  # Random initial solution

    def random_solution(self):
        return self.solution

    def get_neighbors(self, solution):
        neighbors = []
        for i in range(len(solution)):
            neighbor = solution[:]
            neighbor[i] += random.choice([-1, 1])
            neighbors.append(neighbor)
        return neighbors

    def heuristic(self, solution):
        return sum(solution)


problem = ExampleProblem()
print("Initial solution:", problem.solution)
solution = hill_climbing(problem)
print("Final solution:", solution)
