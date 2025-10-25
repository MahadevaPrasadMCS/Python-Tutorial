def mystery(num, cache={}):
    if num in cache:
        return cache[num]
    if num <= 1:
        result = 1
    else:
        result = num * mystery(num - 2)
    cache[num] = result
    return result

print(mystery(5))
print(mystery(6))
print(mystery(5))


"""
Output:
15
48
15
"""
