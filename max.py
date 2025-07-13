def get_max_value(numbers):
    """
    Returns the maximum value from a list of numbers.
    
    :param numbers: List of numeric values
    :return: Maximum value in the list
    """
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
            
    return max_value
