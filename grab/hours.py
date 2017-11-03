def getMinuteEffect(leaveMM,entranceMM):
    minuteDiff = leaveMM - entranceMM
    if(minuteDiff > 0):
        return 1
    else :
        return -1

def getCost(entranceHH, leaveHH,minuteEffect):
    cost = 2
    hourDiff = leaveHH - entranceHH

    if(minuteEffect >0):
        hourDiff += 1

    if (hourDiff == 0):
        return cost
    elif (hourDiff == 1):
        return cost + 3
    else:
        return cost + 3 + 4 * (hourDiff - 1)

def solution(E, L):
    entranceHH = int(E.split(":")[0])
    entranceMM = int(E.split(":")[1])
    leaveHH = int(L.split(":")[0])
    leaveMM = int(L.split(":")[1])
    minuteEffect = getMinuteEffect(leaveMM,entranceMM)
    return getCost(entranceHH, leaveHH, minuteEffect)


E="09:45"
L="11:00"
print(solution(E,L))