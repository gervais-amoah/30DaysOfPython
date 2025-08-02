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