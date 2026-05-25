text = input("textni kiriting: ")

numbers = ""
for i in text:
    if not i.isalpha():
        numbers += i
    else:
        numbers += " "

lst = []
for i in numbers.split():
    lst.append(int(i))

print(len(set(lst)))
