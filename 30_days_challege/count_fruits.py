def count_fruits(fruits):
    """
    Count the occurrences of each type of fruit in the list.

    Args:
    fruits (list): A list of fruits (strings).

    Returns:
    dict: A dictionary with fruit names as keys and their counts as values.
    """
    fruit_count = {}
    
    for fruit in fruits:
        if fruit in fruit_count:
            fruit_count[fruit] += 1
        else:
            fruit_count[fruit] = 1
            
    return fruit_count

# Example usage
if __name__ == "__main__":
    fruits = ["apple", "banana", "orange", "apple", "orange", "banana", "apple"]
    result = count_fruits(fruits)
    print(result)  # Output: {'apple': 3, 'banana': 2, 'orange': 2}def filter_odd_numbers(numbers: list[int]) -> list[int]: