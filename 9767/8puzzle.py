import heapq

# Define the goal state
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i * 3 + j]
            if value != 0:
                goal_row = (value - 1) // 3
                goal_col = (value - 1) % 3
                distance += abs(goal_row - i) + abs(goal_col - j)
    return distance

# Define possible moves
def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    zero_row, zero_col = zero_index // 3, zero_index % 3
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = state[:]
            new_state[zero_index], new_state[new_row * 3 + new_col] = new_state[new_row * 3 + new_col], new_state[zero_index]
            neighbors.append(new_state)
    return neighbors

# Define A* search algorithm
def astar(start_state):
    heap = [(0, 0, start_state, [])]
    closed = set()
    while heap:
        _, g, state, path = heapq.heappop(heap)
        if state == goal_state:
            return path
        if tuple(state) in closed:
            continue
        closed.add(tuple(state))
        h = heuristic(state)
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (g + 1 + h, g + 1, neighbor, path + [neighbor]))
    return None

# Example usage
initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
solution_path = astar(initial_state)
if solution_path:
    print("Steps to reach the goal state:")
    for i, state in enumerate(solution_path):
        print("Step", i + 1, ":")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution found.")
