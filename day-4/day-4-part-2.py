with open('day-4/input.txt') as f:
# with open('day-4/example.txt') as f:
    crossword = f.read()
    # for line in crossword:
    rows = crossword.strip().split()
    sum = 0
    for i in range(len(rows)):
        rows[i] = list(rows[i])
    
    for i in range(len(rows)-2):
        for j in range(len(rows[i])-2):
            if rows[i][j] == 'M' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'S' and rows[i+2][j] == 'S' and rows[i+1][j+1] == 'A' and rows[i][j+2] == 'M':
                sum+=1
            if rows[i][j] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'M' and rows[i+2][j] == 'M' and rows[i+1][j+1] == 'A' and rows[i][j+2] == 'S':
                sum+=1
            if rows[i][j] == 'M' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'S' and rows[i+2][j] == 'M' and rows[i+1][j+1] == 'A' and rows[i][j+2] == 'S':
                sum+=1
            if rows[i][j] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'M' and rows[i+2][j] == 'S' and rows[i+1][j+1] == 'A' and rows[i][j+2] == 'M': 
                sum+=1
    print(sum)