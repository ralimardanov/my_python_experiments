def helper(newstr,text,combiner):
    ind = 0
    while ind < len(text) - 1:
        if combiner == "":
            newstr += text[ind]
        else:
            newstr += text[ind] + combiner
        ind += 1
    newstr += text[-1]
    return newstr

def join(text, combiner="", fordict=""):
    newstr = ""
    if isinstance(text, dict):
        if fordict == "":
            pass
        else:
            while True:
                fordict = input("Please select keys or values: ")
                if fordict == "keys" or fordict == "values":
                    break
                else:
                    print("Please select one of them: keys or values!")
                    continue
        cast_to_str = lambda x: str(x)
        if fordict == "" or fordict == "keys":
            return helper(newstr,list(text.keys()),combiner)
        elif fordict == "values":
            return helper(newstr,list(map(cast_to_str,list(text.values()))),combiner)
    return helper(newstr,text,combiner)

