def tuple_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Example usage
numbers = (2, 3, 4)  # Replace with any tuple of numbers
result = tuple_product(numbers)
print("The product of the tuple is:", result)
