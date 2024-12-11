import re
with open('day-3/input.txt') as f:
# with open('day-3/example-input.txt') as f:
    doDont = re.findall(r"do\(\).*?don't\(\)", f.read())
    print(doDont)
    print(" ")
    sum = 0
    for section in doDont:
        print('section:', section)
        print(" ")
        mulRegex = re.findall(r"mul\((\d*),(\d*)\)", section)

        for multiplicands in mulRegex:
            product = int(multiplicands[0]) * int(multiplicands[1])
            sum += product
    print(sum)



