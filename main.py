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
def merge(matrix):  #adds similar numbers to the left side
    global score
    x = [0]*len(matrix)
    for num in range(len(matrix)):
        c=[]
        for row in matrix[num]:
            if row!=0:
                c.append(row)
        i=0
        while i < len(c)-1:
            if c[i]==c[i+1]:
                score+=c[i]
                c[i]*=2
                del c[i+1]
            i+=1
        while len(c) < len(matrix[num]):
            c.append(0)
        x[num]=c[:]
    return x

def transpose(matrix):    #we use transpose to add similar numbers up and dowm
    new_matrix=[]
    for colomn in range(len(matrix[0])):
        x=[]
        for row in range(len(matrix)):
                       x.append(matrix[row][colomn])
        new_matrix.append(x)
    return new_matrix

def inverse(matrix):   #we use inverse to add numbers to the right
    new_matrix=[]
    for list1 in matrix:
        new_matrix.append(list1[::-1])
    return new_matrix

def move(matrix,movement):  #indicates what keys to use to move the numbers up, down, left or right
    if movement=="8":
        matrix=transpose(merge(transpose(matrix)))
    elif movement=="5":
        matrix=transpose(inverse(merge(inverse(transpose(matrix)))))
    elif movement=="4":
        matrix=merge(matrix)
    elif movement=="6":
        matrix=inverse(merge(inverse(matrix)))
    return matrix

def is_there_space(matrix):   #checks if there is space to randomly import 2 or 4 
    for row in matrix:
        for colomn in row:
            if colomn==0:
                return True
    return False

def is_there_move(matrix):    #checks if there is a potential move by adding two similar numbers
    for row in matrix:
        for i in range(len(row)-1):
            if row[i]==row[i+1]:
               return True
    matrix=transpose(matrix)
    for row in matrix:
        for i in range(len(row)-1):
            if row[i]==row[i+1]:
               return True     
    return False 
