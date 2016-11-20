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

    for i in range(0, n):
        t = StartActivityBinarySearch(activities, activities[i].StartTime)
        optimal[i] = max(optimal[i - 1], optimal[t] + activities[i].Weight)

    return optimal[n - 1]

activities = list()
activities.append(ActivityInfo(1, 0, 3, 20))
activities.append(ActivityInfo(2, 2, 6, 30))
activities.append(ActivityInfo(3, 3, 6, 20))
activities.append(ActivityInfo(4, 2, 10 , 30))

print(ActivitySelector(activities))