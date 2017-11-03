# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    tickets = []
    daysForTheWeek = 0
    weekPointIndexes={}
    weekPointIndexes[7] = []
    weekPointIndexes[14] = []
    weekPointIndexes[21] = []
    weekPointIndexes[28] = []
    for idx, ele in enumerate(A):
        if(ele >= 7 and ele < 14):
            weekPointIndexes[7].append(idx)
            break;
        elif (ele >= 14 and ele < 21):
            weekPointIndexes[14].append(idx)
            break;
        elif (ele >= 21 and ele < 28):
            weekPointIndexes[21].append(idx)
            break;
        elif (ele >= 28):
            weekPointIndexes[28].append(idx)
            break;
    weekPoints = []
    for key,list in weekPointIndexes.iteritems():
        if not list:
            continue
        else:
            weekPoints.append(min(list))
    totalCost = 0
    for weekNo, weekIndex in enumerate(weekPoints):
        perDayTicketCost = (weekIndex+1 - weekNo*7)*2
        if perDayTicketCost <= 7:
            totalCost += perDayTicketCost
        else:
            totalCost += 7

    remainderDayIndexStart = max(weekPoints)+ 1
    totalCost += len(A[remainderDayIndexStart:])*2
    if totalCost > 25 :
        totalCost = 25
    return totalCost

A=[1,2,4,5,7,29,30]
print(solution(A))