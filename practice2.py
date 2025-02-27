def remove_duplicates(lst):
    return list(dict.fromkeys(lst))  # Uses dict to maintain order and remove duplicates

# Example usage
lst = [1, 2, 3, 4, 3, 2, 5, 6, 5, 6, 7]
print(remove_duplicates(lst))  # Output: [1, 2, 3, 4, 5, 6, 7]
