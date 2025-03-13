import numpy as np

def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

def get_neighbors(state):
    neighbors = []
    x, y = np.where(state == 0)
    x, y = int(x), int(y)
    moves = {
        'Up': (x - 1, y),
        'Down': (x + 1, y),
        'Left': (x, y - 1),
        'Right': (x, y + 1)
    }
    
    for move, (nx, ny) in moves.items():
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = state.copy()
            new_state[x, y], new_state[nx, ny] = new_state[nx, ny], new_state[x, y]
            neighbors.append((new_state, move))
    
    return neighbors

def play_8_puzzle():
    print("Welcome to the 8-Puzzle Game!")
    initial_state = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    
    current_state = initial_state.copy()
    
    while not np.array_equal(current_state, goal_state):
        print_puzzle(current_state)
        move = input("Enter move (Up, Down, Left, Right) or 'exit' to quit: ").strip()
        
        if move.lower() == 'exit':
            print("Game exited.")
            return
        
        valid_moves = get_neighbors(current_state)
        valid_moves_dict = {m: s for s, m in valid_moves}
        
        if move in valid_moves_dict:
            current_state = valid_moves_dict[move]
        else:
            print("Invalid move! Try again.")
    
    print("Congratulations! You solved the puzzle!")
    print_puzzle(current_state)

if __name__ == "__main__":
    play_8_puzzle()
