def  analyze_floats_in_text(text:str):
    clean_text = text.replace(","," ")
    data = clean_text.split()
    numbers = []
    dct = {
        "average": float(0),
        "min": float(0),
        "max": float(0)
    }
    
    for i in data:
        try:
            a = float(i)
            numbers.append(a)
        except ValueError:
            pass
    dct['min'] = min(numbers)
    dct['max'] = max(numbers)
    dct["average"] = sum(numbers) / len(numbers)
    return(dct)