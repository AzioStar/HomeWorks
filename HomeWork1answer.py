arr = [int(input(">> ")) for i in range(int(input("nechta son kiritmoqchisiz: ")))]
dct = {}
for i in arr:
    dct.update({i: arr.count(i)})
arr.clear()
for i in dct:  
    arr.append(dct[i])
for i in arr:
    if arr.count(i) > 1:
        print(False)
        break
else:
    print(True)

    