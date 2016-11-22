#Zender Nelson, Mason Urnen, James Musselman
#Comp 569
#Assignment 5, Problem 4.23

# 1Weighted-Activity-Selection(S):  // S = list of activities
# 2 
# 3     sort S by finish time
# 4     opt[0] = 0
# 5    
# 6     for i = 1 to n:
# 7         t = binary search to find activity with finish time <= start time for i
# 8         opt[i] = MAX(opt[i-1], opt[t] + w(i))
# 9         
#10     return opt[n]

import math

class ActivityInfo():
    def __init__(self, activity, startTime, endTime, weight):
        self.Activity = activity
        self.StartTime = startTime
        self.EndTime = endTime
        self.Weight = weight

def StartActivityBinarySearch(activities, startTime):
    return ActivityBinarySearch(activities, startTime, 0, len(activities) - 1)

def ActivityBinarySearch(activities, startTime, startIndex, endIndex):
    if (startIndex == endIndex):
        return startIndex

    midPoint = math.floor((endIndex - startIndex) / 2) + startIndex

    if (activities[midPoint].EndTime <= startTime):
        return ActivityBinarySearch(activities, startTime, midPoint + 1, endIndex)

    return ActivityBinarySearch(activities, startTime, startIndex, midPoint - 1)

def ActivitySelector(activities):
    activities.sort(key=lambda activity: activity.EndTime)

    n = len(activities)

    optimal = [0 for x in range(0,n)]
    endTimes = list(set([activities[x].EndTime for x in range(0,n)]))

    endTimes.sort()
    k = len(endTimes)
    
    for j in range(1,k):
        max = optimal[j-1]

        for i in range(1,n):
            if (activities[i].EndTime == endTimes[j]):
                newValue = activities[i].Weight + optimal[0]
                if (newValue > max):
                    max = newValue

        optimal[j] = max

    return optimal

activities = list()
# activities.append(ActivityInfo(3, 3, 6, 20))
# activities.append(ActivityInfo(1, 0, 3, 20))
# activities.append(ActivityInfo(2, 2, 6, 30))
# activities.append(ActivityInfo(4, 2, 10 , 30))

with open('schedules.txt') as f:
    print("Inputed Schedules")
    for line in f:
        int_list = list()

        #---Printing schedules---
        print("(", end="")
        count = 0
        for i in line.split():
            count += 1
            int_list.append(int(i))
            print(i, end="")
            if (count == 4):
                print(")")
            else:
                print(", ", end="")

        activities.append(ActivityInfo(int_list[0], int_list[1], int_list[2], int_list[3]))

print(ActivitySelector(activities))
