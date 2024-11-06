def vf(td, tv):
  
    return list(td.values()).count(tv)


td = {'a': 1, 'b': 2, 'c': 1, 'd': 3} 
tv = 1 
frequency = vf(td, tv)

print(f"The frequency of {tv} in the dictionary is:", frequency)
