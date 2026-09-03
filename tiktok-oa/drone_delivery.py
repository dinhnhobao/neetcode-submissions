def drone_delivery(target, stations):
    if not stations:
        return 0 if target == 0 else -1
    stations = sorted(stations)
    n = len(stations)
    steps = 0
    index = 0
    current = 0
    
    while current < target:
        # skip stations behind current
        while index < n and stations[index] < current:
            index += 1
        
        if index >= n: # last step
            steps += target - current
            current = target
        else: # normal step
            steps += stations[index] - current
            current = stations[index] + 10
            if current > target:
                current = target
    return steps
             
print(drone_delivery(30, [5, 16])) # 10