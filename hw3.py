def tp(numbers):
    pro = 1
    for num in numbers:
        pro *= num
    return pro


numbers = (2, 3, 4)  
result = tp(numbers)
print("The product of the tuple is:", result)
