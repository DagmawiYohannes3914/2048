import os
import random

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
        
def generation(grid,first_gen=False):#this will generate the numbers that we will use to play
    global grid_size#call the variable grid from out side
    first_row=random.randint(0,grid_size-1)
    first_colomn=random.randint(0,grid_size-1)
    first_generation=[2,2,2,2,4]#the numbers we use 
    if first_gen==True:#when we first start the game it will generate 2 numbers
        grid[first_row][first_colomn]=random.choice(first_generation)
    
    while grid[first_row][first_colomn]!=0:#After the game have been started it will only generate one number randomly
        first_row=random.randint(0,grid_size-1)
        first_colomn=random.randint(0,grid_size-1)
        
    grid[first_row][first_colomn]=random.choice(first_generation)
    return grid
