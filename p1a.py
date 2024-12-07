def linear_search(arr, target):
    # Iterate through the list
    for index, value in enumerate(arr):
        if value == target:  # If target is found
            return index  # Return the index of the target
    return -1  # Return -1 if target is not found

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
