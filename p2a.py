def insert_into_sorted_list(sorted_list, element):
    # Insert element into the sorted list while maintaining the order
    sorted_list.append(element)  # Add the element to the end of the list
    sorted_list.sort()  # Sort the list to maintain order
    return sorted_list

# Example usage
sorted_list = [1, 3, 5, 7, 9]
element = 6

print("Original Sorted List:", sorted_list)
sorted_list = insert_into_sorted_list(sorted_list, element)
print("Updated Sorted List:", sorted_list)
