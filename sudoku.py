# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 08:39:40 2018

@author: martin.isusi.seff
"""

def valueexists(array, number):
    exists = False
    for n in array:
        if number == n:
            exists = True
            break
    return exists

def validatesudoku(sudoku):
    #Validate rows
    for row in sudoku:
        possiblevalues = [1,2,3,4,5,6,7,8,9]
        for column in row:
            if column != -1:
                if valueexists(possiblevalues, column):
                    possiblevalues.remove(column)
        if len(possiblevalues) != 0:
            #print(possiblevalues)
            return False
    #Validate columns
    for column in range(9):
        possiblevalues = [1,2,3,4,5,6,7,8,9]
        for row in range(9):
            if column != -1:
                if valueexists(possiblevalues, sudoku[row][column]):
                    possiblevalues.remove(sudoku[row][column])
        if len(possiblevalues) != 0:
            print(possiblevalues)
            return False
    #Validate submatrix
    for n in range(0,9,3):
        possiblevalues = [1,2,3,4,5,6,7,8,9]
        for row in range(n, n+3):
            for column in range(n, n+3):
                if column != -1:
                    if valueexists(possiblevalues, sudoku[row][column]):
                        possiblevalues.remove(sudoku[row][column])
        if len(possiblevalues) != 0:
            return False
    return True

def getpossiblevalues(sudoku, row, column):
    possiblevalues = [1,2,3,4,5,6,7,8,9]
    #Search non-possible values based on the row and remove from possiblevalues
    for i in range(9):
        if i != column and sudoku[row][i] != -1:
            if valueexists(possiblevalues, sudoku[row][i]):
                possiblevalues.remove(sudoku[row][i])
    #Search non-possible values based on column and remove from possiblevalues
    for i in range(9):
        if i != row and sudoku[i][column] != -1:
            if valueexists(possiblevalues, sudoku[i][column]):
                possiblevalues.remove(sudoku[i][column])
    #Search non-possible values based on sub matrix and remove from 
    #possiblevalues.
    #First, calculate row range, that will depende on the row.
    rowrange = []
    columnrange = []
    if row == 0 or row == 3 or row == 6:
        rowrange = [row, row + 1, row + 2]
    elif row == 2 or row == 5 or row == 8:
        rowrange = [row - 2, row - 1, row]
    else:
        rowrange = [row - 1, row, row +1]
    #Calculate column range, that will depende on the row.
    if column == 0 or column == 3 or column == 6:
        columnrange = [column, column + 1, column + 2]
    elif column == 2 or column == 5 or column == 8:
        columnrange = [column - 2, column - 1, column]
    else:
        columnrange = [column - 1, column, column + 1]
    #Iterate through the row and column range to chech the possible values.
    for rowindex in rowrange:
        for columnindex in columnrange:
            if rowindex != row and columnindex != column and sudoku[rowindex][columnindex] != -1:
                if valueexists(possiblevalues, sudoku[rowindex][columnindex]):
                    possiblevalues.remove(sudoku[rowindex][columnindex])
    return possiblevalues
        
def getallemptycells(sudoku):
    emptycells = []
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == -1:
                possiblevalues = getpossiblevalues(sudoku,row,column)
                emptycell = [row, column, possiblevalues]
                emptycells.append(emptycell)
    #Sort empty cells by amount of possible values.
    emptycells = sort(emptycells)
    return emptycells
                
def merge(a, b):
    a_index = 0
    b_index = 0
    z = []
    while a_index<len(a) or b_index<len(b):
        if a_index == len(a):
            z.append(b[b_index])
            b_index = b_index + 1
        elif b_index == len(b):
            z.append(a[a_index])
            a_index = a_index + 1
        elif len(a[a_index][2])<len(b[b_index][2]):
            z.append(a[a_index])
            a_index = a_index + 1
        else:
            z.append(b[b_index])
            b_index = b_index + 1
    return z

def sort(array):
    array_sorted = []
    a = array[0:int(len(array)/2)]
    b = array[int(len(array)/2):len(array)]
    if len(a)>1:
        a = sort(a)
    
    if len(b)>1:
        b = sort(b)
    
    array_sorted = merge(a, b)
    return array_sorted

"""
1.1 When function is called, if there are not empty cells in the incoming
sudoku, validate it and return the sudoku matrix if it's ok or False if it's
not ok.

1.2 If there are empty cells, but the first one (as they are ordered) does not
have any possible value, return false as it is considered that if an empty
cell does not have a possible value, there must be incorrect values in the 
matrix

2.0 Iterative approach (for simple sudokus). If the sudoku is solved, return
the complete matrix. If it is not solved, recursive approach will be executed.

3.0 Recursive approach (for harder sudokus, if iterative approach did not work)
"""

def solvesudoku(sudoku):
    emptycells = getallemptycells(sudoku)
    ###########################################################################
    #1.1
    if len(emptycells) == 0:
        if validatesudoku(sudoku):
            return sudoku
        else:
            return False
    ###########################################################################
    #1.2
    elif len(emptycells[0][2]) == 0:
        return False
    ###########################################################################
    #2.0 - Iterative approach
    emptycellfilled = (len(emptycells[0][2]) == 1)
    while emptycellfilled:
        for emptycell in emptycells:
            if len(emptycell[2]) == 1:
                row = emptycell[0]
                column = emptycell[1]
                sudoku[row][column] = emptycell[2][0]
                emptycellfilled = True
            else:
                break
        emptycells = getallemptycells(sudoku)
        if len(emptycells) > 0:
            emptycellfilled = len(emptycells[0][2]) == 1
        else:
            break
    if len(emptycells) == 0:
        return sudoku
    ###########################################################################
    #3.0 - Recursive approach
    i = 0
    while i in range(len(emptycells)):
        z = 0
        while z in range(len(emptycells[i][2])):
            #print("sarasa")
            newsudoku = list(sudoku)
            newsudoku[emptycells[i][0]][emptycells[i][1]] = emptycells[i][2][z]
            testsudoku = solvesudoku(newsudoku)
            if testsudoku != False:
                print(testsudoku)
            if testsudoku != False and len(testsudoku) !=0:
                #print("todo ok")
                return testsudoku
            z += 1
        i += 1
    return False

def printsudoku(sudoku):
    for i in sudoku:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6],
              "\t",i[7],"\t",i[8],"\t")

###############################################################################

""" Difícil 
sudoku = [[-1,8,-1,6,9,3,-1,-1,-1],
          [-1,2,-1,5,-1,-1,-1,-1,4],
          [-1,7,-1,-1,8,4,3,5,-1],
          [-1,-1,-1,-1,7,-1,8,-1,-1],
          [-1,3,7,8,2,-1,-1,-1,-1],
          [-1,-1,4,-1,-1,-1,-1,-1,-1],
          [-1,-1,3,-1,-1,-1,-1,-1,7],
          [-1,4,-1,-1,-1,2,-1,-1,6],
          [-1,5,2,7,6,-1,-1,-1,-1]]
"""
"""
sudoku =[[-1,-1,-1,6,3,7,-1,-1,-1],
         [-1,2,9,-1,1,-1,-1,-1,-1],
         [8,3,-1,9,2,5,4,1,-1],
         [-1,7,8,2,-1,6,1,-1,-1],
         [9,6,-1,8,7,1,5,-1,3],
         [5,1,2,-1,-1,4,-1,6,-1],
         [4,8,1,5,6,9,-1,-1,-1],
         [-1,-1,-1,-1,8,2,6,-1,4],
         [2,9,6,7,4,-1,-1,-1,-1]]
"""

sudoku =[[-1,5,3,-1,-1,9,-1,7,6],
         [-1,-1,-1,1,-1,-1,8,-1,-1],
         [-1,-1,-1,-1,-1,-1,5,-1,-1],
         [-1,3,6,2,-1,-1,-1,-1,8],
         [-1,-1,4,3,8,7,-1,5,2],
         [7,8,-1,-1,6,-1,-1,-1,3],
         [3,2,7,-1,-1,-1,-1,-1,-1],
         [4,6,-1,5,-1,-1,-1,2,-1],
         [-1,-1,-1,7,-1,4,-1,-1,-1]]
#print(validatesudoku(sudoku))
solvedsudoku = solvesudoku(sudoku)
printsudoku(solvedsudoku)
print(">>",validatesudoku(solvedsudoku))

#printsudoku(sudoku)
#print(validatesudoku(sudoku))