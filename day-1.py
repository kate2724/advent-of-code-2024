# TODO

# Take in the lists

col1 = []
col2 = []
with open('input.txt', 'r') as f:
    for line in f:
        num1, num2 = line.strip().split()
        col1.append(int(num1))
        col2.append(int(num2))

# Order the two lists smallest to largest
col1.sort()
col2.sort()

# Abs value of list1 - list2

totalDistance = 0

for i in range(len(col1)):
    totalDistance += abs(col1[i] - col2[i])

print(totalDistance)


similarityScore = 0
# for each number in left list, find how common in right list
for i in range(len(col1)):
    count = col2.count(col1[i])
    product = col1[i] * count
    similarityScore += product

print(similarityScore)
# multiply that number by the number of times it appears in the right list
# Sum the products
#