def tricky(lst=[]):
    lst.append(len(lst))
    return lst

print(tricky())
print(tricky())
print(tricky([1, 2]))
print(tricky())

"""
Output:
[0]
[0, 1]
[1, 2, 2]
[0, 1, 2]

"""