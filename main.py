def game_matrix(): #this will do the n by n grid
    global grid_size
    matrix=[0] * grid_size
    for row in range(grid_size):
        matrix[row]=[0] * grid_size
    return matrix