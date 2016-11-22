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
import copy

class ActivityInfo():
    def __init__(self, startTime, endTime, weight):
        self.StartTime = startTime
        self.EndTime = endTime
        self.Weight = weight

class OptimalInfo():
    def __init__(self):
        self.ActivityList = list()
        self.Profit = 0
    def AddActivity(self, activity, profit):
        self.ActivityList.append(activity)
        self.Profit += profit

def StartActivityBinarySearch(endTimes, startTime):
    return ActivityBinarySearch(endTimes, startTime, 0, len(activities) - 1)

def ActivityBinarySearch(endTimes, startTime, startIndex, endIndex):
    if (startIndex == endIndex):
        return startIndex

    midPoint = math.floor((endIndex - startIndex) / 2) + startIndex

    if (endTimes[midPoint] <= startTime):
        return ActivityBinarySearch(endTimes, startTime, midPoint, endIndex)

    return ActivityBinarySearch(endTimes, startTime, startIndex, midPoint - 1)

def ActivitySelector(activities):
    activities.sort(key=lambda activity: activity.EndTime)

    n = len(activities)

    optimal = [OptimalInfo() for x in range(0,n)]
    endTimes = list(set([activities[x].EndTime for x in range(0,n)]))
    endTimes.append(0)

    endTimes.sort()
    k = len(endTimes)
    
    for j in range(1,k):
        max = optimal[j - 1]

        for i in range(0,n):
            if (activities[i].EndTime == endTimes[j]):
                newOptimal = copy.deepcopy(optimal[StartActivityBinarySearch(endTimes, activities[i].StartTime)])
                newOptimal.AddActivity(i, activities[i].Weight)
                if (newOptimal.Profit > max.Profit):
                    max = newOptimal

        optimal[j] = max

    return optimal[k-1]

activities = list()

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
            if (count == 3):
                print(")")
            else:
                print(", ", end="")

        activities.append(ActivityInfo(int_list[0], int_list[1], int_list[2]))

print()

optimal = ActivitySelector(activities)

print("Activity Indexes: " + str(optimal.ActivityList))
print("Profit: " + str(optimal.Profit))