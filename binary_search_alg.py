def bsearch(llist, whattofind):
    slist = sorted(llist)
    midind = len(slist) // 2
    if whattofind in slist:
        if whattofind == slist[midind]:
            return f"It's middle number. Number: {slist[midind]}; Index: {midind}"
        elif whattofind > slist[midind]:
            for ind,value in enumerate(slist[midind+1::]):
                if value == whattofind:
                    return f"It's larger number. Number: {whattofind}; Index: {ind}"
        elif whattofind < slist[midind]:
            for ind,value in enumerate(slist[:midind]):
                if value == whattofind:
                    return f"It's smaller number. Number: {whattofind}; Index: {ind}"
    else:
        return "Not in the list"