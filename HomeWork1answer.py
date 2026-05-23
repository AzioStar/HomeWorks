import problem1 as p

result = p.last_unique_character(input("Matn kiriting: "))
if result:
    print(f"Eng oxirgi belgi: {result[-1]}")
else:
    print("_")