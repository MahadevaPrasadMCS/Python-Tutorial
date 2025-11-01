class Test:
    data = []

a = Test()
b = Test() #shares same data , because objects ahre their memory
a.data.append(1)
print(b.data)
