import re
with open('day-3/input.txt') as f:
    mulRegex = re.findall(r"mul\((\d*),(\d*)\)", f.read())
    sum = 0
    for multiplicands in mulRegex:
        product = int(multiplicands[0]) * int(multiplicands[1])
        sum += product
    print(sum)



