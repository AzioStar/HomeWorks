def is_sorted(matn: str):
    sonlar = ""
    for i in matn:
        if i.isdigit():
            sonlar += i
        else:
            sonlar += " "

    lst = []
    for i in sonlar.split():
        lst.append(int(i))

    return lst == sorted(lst)

print(is_sorted("a123k456k789l1"))
