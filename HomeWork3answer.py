lst = [6, 5, 4, 8]

lst2 = []
for i in lst: 
    n = 0
    for j in lst:
        if i > j:
            n+=1
    lst2.append(n)
print(lst2)
