### Sliding Window
def count_alternating_parity_subarrays(values):
    if not values:
        return 0
    count = 0
    left, right = 0, 0
    while (right < len(values)):
        if (right == left) or values[right] % 2 != values[right-1] % 2: # different parity
            count += right - left + 1
            right += 1
        else: # update left
            left = right
    return count

print(count_alternating_parity_subarrays([2, 4, 1, 3, 6])) # 7