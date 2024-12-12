import re
import numpy
with open('day-4/input.txt') as f:
# with open('day-4/example.txt') as f:
    crossword = f.read()
    forwards=crossword.count('XMAS')
    backwards=crossword.count('SAMX')
    vertical=0
    backwardsVertical=0
    diagonal=0
    # for line in crossword:
    rows = crossword.strip().split()
    for i in range(len(rows)):
        rows[i] = list(rows[i])
    
    for i in range(len(rows)-3):
        for j in range(len(rows[i])-3):
            if rows[i][j] == 'X' and rows[i+1][j+1] == 'M' and rows[i+2][j+2] == 'A' and rows[i+3][j+3] == 'S':
                diagonal+=1
            if rows[i][j] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'M' and rows[i+3][j+3] == 'X':
                diagonal+=1
            if rows[i][j+3] == 'X' and rows[i+1][j+2] == 'M' and rows[i+2][j+1] == 'A' and rows[i+3][j] == 'S':
                diagonal+=1
            if rows[i][j+3] == 'S' and rows[i+1][j+2] == 'A' and rows[i+2][j+1] == 'M' and rows[i+3][j] == 'X':
                diagonal+=1
    for i in range(len(rows)-3):
        for j in range(len(rows[i])):
            if rows[i][j] == 'X' and rows[i+1][j] == 'M' and rows[i+2][j] == 'A' and rows[i+3][j] == 'S':
                vertical+=1
            if rows[i][j] == 'S' and rows[i+1][j] == 'A' and rows[i+2][j] == 'M' and rows[i+3][j] == 'X':
                backwardsVertical+=1

    # print(forwards)
    # print(backwards)
    # print(vertical)
    # print(backwardsVertical)
    # print(diagonal)
    sum = forwards + backwards + vertical + backwardsVertical + diagonal
    print(sum)