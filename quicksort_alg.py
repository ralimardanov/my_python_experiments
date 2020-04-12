import random

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    main, slist, mlist, llist = random.choice(numbers), [], [], []
    for x in numbers:
        if x < main:
            slist.append(x)
        elif x == main:
            mlist.append(x)
        else:
            llist.append(x)
    return sorted(slist) + mlist + sorted(llist) 

result = quicksort([1,2,3,4,5,5,5,5,12,31,121,11]) 
print(result)