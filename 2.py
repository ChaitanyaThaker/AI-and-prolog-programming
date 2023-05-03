from queue import Queue

# function to find all the possible next states
def next_states(state, capacities):
    x, y = state
    a, b = capacities
    # fill x
    yield (a, y)
    # fill y
    yield (x, b)
    # empty x
    yield (0, y)
    # empty y
    yield (x, 0)
    # pour x into y
    dx = min(x, b - y)
    yield (x - dx, y + dx)
    # pour y into x
    dy = min(y, a - x)
    yield (x + dy, y - dy)

# function to solve the Water Jug Problem
def water_jug_problem(capacities, goal):
    start = (0, 0)
    q = Queue()
    q.put(start)
    visited = set()
    visited.add(start)
    while not q.empty():
        state = q.get()
        if state == goal:
            return True
        for next_state in next_states(state, capacities):
            if next_state not in visited:
                q.put(next_state)
                visited.add(next_state)
    return False

# get user input for capacities
capacities = tuple(map(int, input("Enter the capacities of the two jugs: ").split()))

# get user input for goal
goal = tuple(map(int, input(f"Enter the goal amount of water (less than {max(capacities)}): ").split()))

# check if the goal can be reached with the given capacities
if water_jug_problem(capacities, goal):
    print(f"{goal} can be measured with jugs of {capacities} capacity")
else:
    print(f"{goal} cannot be measured with jugs of {capacities} capacity")
