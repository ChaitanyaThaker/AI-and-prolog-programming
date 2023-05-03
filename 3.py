from queue import Queue, LifoQueue

# Function to get the index of the blank tile in the puzzle state
def get_blank_tile_index(state):
    return state.index(0)

# Function to get the possible moves from the current state
def get_possible_moves(state):
    moves = []
    blank_index = get_blank_tile_index(state)

    # Check if blank tile can move up
    if blank_index not in [0, 1, 2]:
        moves.append('up')

    # Check if blank tile can move down
    if blank_index not in [6, 7, 8]:
        moves.append('down')

    # Check if blank tile can move left
    if blank_index not in [0, 3, 6]:
        moves.append('left')

    # Check if blank tile can move right
    if blank_index not in [2, 5, 8]:
        moves.append('right')

    return moves

# Function to move the blank tile in the given direction
def move_blank_tile(state, direction):
    blank_index = get_blank_tile_index(state)
    new_state = state.copy()

    if direction == 'up':
        new_state[blank_index], new_state[blank_index-3] = new_state[blank_index-3], new_state[blank_index]
    elif direction == 'down':
        new_state[blank_index], new_state[blank_index+3] = new_state[blank_index+3], new_state[blank_index]
    elif direction == 'left':
        new_state[blank_index], new_state[blank_index-1] = new_state[blank_index-1], new_state[blank_index]
    elif direction == 'right':
        new_state[blank_index], new_state[blank_index+1] = new_state[blank_index+1], new_state[blank_index]

    return new_state

# Function to perform BFS search
def bfs(initial_state, goal_state):
    visited_states = set()
    queue = Queue()

    # Add the initial state to the queue
    queue.put(initial_state)

    # Loop until the queue is empty
    while not queue.empty():
        # Get the next state from the queue
        current_state = queue.get()

        # Check if the current state is the goal state
        if current_state == goal_state:
            # Return the path from the initial state to the goal state
            return visited_states

        # Add the current state to the visited states set
        visited_states.add(tuple(current_state))

        # Get the possible moves from the current state
        possible_moves = get_possible_moves(current_state)

        # Loop through the possible moves and add the new states to the queue
        for move in possible_moves:
            new_state = move_blank_tile(current_state, move)

            # Check if the new state has already been visited
            if tuple(new_state) not in visited_states:
                queue.put(new_state)
                visited_states.add(tuple(new_state))

    # If the goal state cannot be reached, return None
    return None

# Function to perform DFS search
def dfs(initial_state, goal_state):
    visited_states = set()
    stack = LifoQueue()

    # Add the initial state to the stack
    stack.put(initial_state)

    # Loop until the stack is empty
    while not stack.empty():
        # Get the next state from the stack
       
        current_state = stack.get()

        # Check if the current state is the goal state
        if current_state == goal_state:
            # Return the path from the initial state to the goal state
            return visited_states

        # Add the current state to the visited states set
        visited_states.add(tuple(current_state))

        # Get the possible moves from the current state
        possible_moves = get_possible_moves(current_state)

        # Loop through the possible moves and add the new states to the stack
        for move in possible_moves:
            new_state = move_blank_tile(current_state, move)

            # Check if the new state has already been visited
            if tuple(new_state) not in visited_states:
                stack.put(new_state)
                visited_states.add(tuple(new_state))

    # If the goal state cannot be reached, return None
    return None

# Function to print the path from the initial state to the goal state
def print_path(path):
    for state in path:
        for i in range(3):
            print(state[i*3:i*3+3])
        print()

# Get the initial state from the user
initial_state = [int(x) for x in input('Enter the initial state: ').split()]

# Get the goal state from the user
goal_state = [int(x) for x in input('Enter the goal state: ').split()]

# Get the search method from the user
method = input('Enter the method (BFS or DFS): ')

# Perform the search using the chosen method
if method.lower() == 'bfs':
    path = bfs(initial_state, goal_state)
elif method.lower() == 'dfs':
    path = dfs(initial_state, goal_state)
else:
    print('Invalid method entered!')
    path = None

# Print the path from the initial state to the goal state
if path is not None:
    print('Path from initial state to goal state:')
    print_path(path)
    print(goal_state)
else:
    print('Goal state cannot be reached from initial state using the chosen method.')