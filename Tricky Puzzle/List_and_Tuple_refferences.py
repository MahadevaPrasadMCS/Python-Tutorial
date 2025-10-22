lst = [1, 2, 3]
gen = (x * x for x in lst)
lst.append(4)
print(list(gen))
print(list(gen))

"""
Output:
[1, 4, 9, 16]
[]
"""
