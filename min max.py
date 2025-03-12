def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)

# Example usage
arr = [64, 25, 12, 22, 11, 90, 33, 21]
min_val, max_val = find_min_max(arr)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")
