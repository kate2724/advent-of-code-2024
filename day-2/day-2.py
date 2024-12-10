# check if numbers are all increasing
    # if not, return unsafe
# check if numbers are all decreasing
    # if not, return unsafe
# check that numbers differ by at least 1 (not the same)
# check that numbers differ by at most 3


safeReportsCount = 0
# with open('day-2/input-day2.txt', 'r') as f:
with open('day-2/example-input.txt', 'r') as f:
    for line in f:
        safe=True
        report = line.strip().split()
        for i in range(len(report)):
            report[i] = int(report[i])
        for i in range(len(report)-1):
            absDiff = abs(report[i] - report[i+1])
            if absDiff > 3 or absDiff==0:
                safe = False

        increasing = []
        increasing.extend(report)
        increasing.sort()
        
        decreasing = []
        decreasing.extend(report)
        decreasing.sort(reverse=True)

        if decreasing != report and increasing != report:
            safe = False
        if(safe):
            safeReportsCount += 1
            
print(safeReportsCount)
            