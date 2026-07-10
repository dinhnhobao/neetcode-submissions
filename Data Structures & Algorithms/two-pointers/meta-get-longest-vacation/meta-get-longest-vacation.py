"""
https://www.1point3acres.com/interview/thread/1168658

2. You're given a calendar year represented as a char array containing either H or W where:
H = Holiday
W = Workday
Given a number of Personal Time-Off days (PTO), maximize the length of the longest vacation you can take. No rollovers.
Example:
[W, H, H, W, W, H, W], PTO = 2 -> return 5

Have a sliding window and the window should only contain at most PTO number of Workdays

             l
[W, H, H, W, W, H, W], PTO = 2 -> return 5
                   r

count 2
maximum 4 

"""

def get_longest_vacation(days, k):
    if not days:
        return 0
    left, count, maximum = 0, 0, 0
    for right in range(len(days)):
        if days[right] == 'W':
            count += 1
        if count > k:
            while days[left] == 'H': # find the next W
                left += 1
            # stops when days[left] == 'W', skip over it
            left += 1
            count -= 1
        maximum = max(maximum, right-left+1)
    return maximum

print(get_longest_vacation(['W', 'H', 'H', 'W', 'W', 'H', 'W'], 2))
        
        