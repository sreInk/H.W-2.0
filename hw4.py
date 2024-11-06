def value_frequency(test_dict, target_value):
    # Count how many times the target_value appears in the dictionary values
    return list(test_dict.values()).count(target_value)

# Example usage
test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}  # Replace with any dictionary
target_value = 1  # Replace with the value you want to check
frequency = value_frequency(test_dict, target_value)

print(f"The frequency of {target_value} in the dictionary is:", frequency)
