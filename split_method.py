def split(text, separator=" ", count=0):
    listtoreturn, listforalloccurences, strtoappend = [], [], ""

    if count == 0:
        if separator in text:
            ind = 0
            while ind < len(text):
                if text[ind : ind + len(separator)] == separator:
                    listtoreturn.append(strtoappend)
                    strtoappend = ""
                    ind = ind + len(separator)
                else:
                    strtoappend += text[ind]
                    ind += 1
            if strtoappend != "":
                listtoreturn.append(strtoappend)
        else:
            listtoreturn.append(text)

    else:
        if separator in text:
            localcount, ind = 0, 0
            while ind < len(text) and localcount < count:
                if text[ind : ind + len(separator)] == separator:
                    listtoreturn.append(strtoappend)
                    strtoappend = ""
                    ind = ind + len(separator)
                    localcount += 1
                else:
                    strtoappend += text[ind]
                    ind += 1

            for index, _ in enumerate(text):
                if text[index : index + len(separator)] == separator:
                    listforalloccurences.append(index)

            if strtoappend != "":
                listtoreturn.append(strtoappend)
            elif count < len(listforalloccurences):
                listtoreturn.append(text[ind::])
        else:
            listtoreturn.append(text)

    return listtoreturn
