def last_unique_character(text: str):
    lst = []
    lst.extend(text)
    text1 = ""
    for i in lst:
        if lst.count(i) < 2:
            text1 += f" {"".join(i)}"
    print(text1)
    return text1