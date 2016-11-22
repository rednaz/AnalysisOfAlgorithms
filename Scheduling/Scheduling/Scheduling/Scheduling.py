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
    def __init__(self, activity, startTime, endTime, weight):
        self.Activity = activity
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
activities.append(ActivityInfo(1, 0, 3, 20))
activities.append(ActivityInfo(2, 2, 6, 30))
activities.append(ActivityInfo(3, 3, 6, 20))
activities.append(ActivityInfo(4, 2, 10 , 30))

optimal = ActivitySelector(activities)

print(optimal.ActivityList)
print(optimal.Profit)

# with open('schedules.txt') as f:
#     for line in f:
#         int_list = [int(i) for i in line.split()]
#         activities.append(ActivityInfo(int_list(0), int_list(1), int_list(2),
#         int_list(3)))
#         print int_list
print(ActivitySelector(activities))