def isIncreasing(report):
    increasing = []
    increasing.extend(report)
    increasing.sort()
    if increasing != report:
        return False
    return True

def isDecreasing(report):
    decreasing = []
    decreasing.extend(report)
    decreasing.sort(reverse=True)
    if decreasing != report:
        return False
    return True

def noConsecutiveRepeats(report):
    for i in range(len(report)-1):
        if report[i] == report[i+1]:
            return False
    return True

def noMoreThanThree(report):
    for i in range(len(report)-1):
        absDiff = abs(report[i] - report[i+1])
        if absDiff > 3:
            return False
    return True

safeReportsCount = 0
with open('day-2/input-day2.txt', 'r') as f:
# with open('day-2/example-input.txt', 'r') as f:
    for line in f:
        badLevelCount = 0
        safe=False
        report = line.strip().split()
        for i in range(len(report)):
            report[i] = int(report[i])
        
        # all increasing 
        increasing = isIncreasing(report)
        decreasing = isDecreasing(report)
        if not increasing and not decreasing: # If report is neither all increasing nor all decreasing
            for i in range(len(report)): # delete each element from list and check if remaining elements are valid
                reportSection = report[:]
                reportSection.pop(i)
                increasing = isIncreasing(reportSection)
                decreasing = isDecreasing(reportSection)
                if increasing or decreasing:
                    if noConsecutiveRepeats(reportSection) and noMoreThanThree(reportSection):
                        safeReportsCount += 1
                        break
                        
        else: # If report is all increasing or all decreasing
            if noConsecutiveRepeats(report) and noMoreThanThree(report):
                safeReportsCount += 1
            else:
                for i in range(len(report)):
                    reportSection = report[:]
                    reportSection.pop(i)
                    noConsecRepeats = noConsecutiveRepeats(reportSection)
                    notMoreThanThree = noMoreThanThree(reportSection)
                    if noConsecRepeats and notMoreThanThree:
                        safeReportsCount += 1
                        break
    print(safeReportsCount)


