from collections import deque

# Define the capacities of the jugs
jug1_capacity = 4
jug2_capacity = 3
target_volume = 2

# Define the initial state
initial_state = (0, 0)

# Define the actions
actions = [
    ("Fill Jug 1", lambda state: (jug1_capacity, state[1])),
    ("Fill Jug 2", lambda state: (state[0], jug2_capacity)),
    ("Empty Jug 1", lambda state: (0, state[1])),
    ("Empty Jug 2", lambda state: (state[0], 0)),
    ("Pour Jug 1 to Jug 2", lambda state: (
        max(0, state[0] - (jug2_capacity - state[1])),
        min(jug2_capacity, state[0] + state[1]))
    ),
    ("Pour Jug 2 to Jug 1", lambda state: (
        min(jug1_capacity, state[0] + state[1]),
        max(0, state[1] - (jug1_capacity - state[0])))
    )
]

def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        if state[0] == target_volume or state[1] == target_volume:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for action_name, action_func in actions:
            new_state = action_func(state)
            if new_state not in visited:
                queue.append((new_state, path + [action_name]))

    return None

def main():
    solution = bfs(initial_state)
    if solution:
        print("Solution found:")
        for i, step in enumerate(solution):
            print(f"Step {i + 1}: {step}")
    else:
        print("No solution found.")

if _name_ == "_main_":
    main()