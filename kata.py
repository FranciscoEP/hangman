def xo(s):
    dict_counter = {}
    for letter in s:
        if letter == "o":
            dict_counter["o"] = s.count(letter)
        
        if letter == "s":
             dict_counter["s"] = s.count(letter) 
        
        else:
            continue
    return print(dict_counter["o"] == dict_counter["s"])
xo("osxxosos")