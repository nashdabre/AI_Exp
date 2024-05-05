import heapq
import itertools

class PuzzleNode:
    def _init_(self, puzzle, parent=None, move=None, depth=0):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = depth + self.heuristic()

    def _lt_(self, other):
        return self.cost < other.cost

    def _eq_(self, other):
        return self.puzzle == other.puzzle

    def _hash_(self):
        return hash(str(self.puzzle))

    def is_goal(self):
        return self.puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def heuristic(self):
        return sum(1 if self.puzzle[i] != 0 and self.puzzle[i] != i + 1 else 0 for i in range(8))

    def get_successors(self):
        successors = []
        i = self.puzzle.index(0)
        if i % 3 != 0:
            new_puzzle = self.puzzle[:]
            new_puzzle[i], new_puzzle[i - 1] = new_puzzle[i - 1], new_puzzle[i]
            successors.append(PuzzleNode(new_puzzle, self, "Left", self.depth + 1))
        if i % 3 != 2:
            new_puzzle = self.puzzle[:]
            new_puzzle[i], new_puzzle[i + 1] = new_puzzle[i + 1], new_puzzle[i]
            successors.append(PuzzleNode(new_puzzle, self, "Right", self.depth + 1))
        if i > 2:
            new_puzzle = self.puzzle[:]
            new_puzzle[i], new_puzzle[i - 3] = new_puzzle[i - 3], new_puzzle[i]
            successors.append(PuzzleNode(new_puzzle, self, "Up", self.depth + 1))
        if i < 6:
            new_puzzle = self.puzzle[:]
            new_puzzle[i], new_puzzle[i + 3] = new_puzzle[i + 3], new_puzzle[i]
            successors.append(PuzzleNode(new_puzzle, self, "Down", self.depth + 1))
        return successors

    def get_solution(self):
        solution = []
        node = self
        while node.parent is not None:
            solution.append(node.move)
            node = node.parent
        return solution[::-1]

def a_star_search(initial_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, initial_state)
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node)
        if current_node.is_goal():
            return current_node.get_solution()
        successors = current_node.get_successors()
        for successor in successors:
            if successor not in closed_set:
                heapq.heappush(open_list, successor)

def print_solution(solution):
    for step, move in enumerate(solution, start=1):
        print(f"Step {step}: Move {move}")

def main():
    initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    initial_node = PuzzleNode(initial_state)
    solution = a_star_search(initial_node)
    if solution:
        print_solution(solution)
    else:
        print("No solution found.")

if _name_ == "_main_":
    main()