def game_matrix(): #this will do the n by n grid
    global grid_size
    matrix=[0] * grid_size
    for row in range(grid_size):
        matrix[row]=[0] * grid_size
    return matrix

def display_game_matrix(grid):# it will diplay the grid
    for row in grid:
        for i in row:
            print('  ',i,end='  ')
        print()