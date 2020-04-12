import string

def caesar_enc(text, num):
    newstr = ""
    lower, upper = string.ascii_lowercase, string.ascii_uppercase
    for value in text:
        if value.isalpha():
            if value.islower():
                for index,val in enumerate(lower):
                    if value == val: newstr += lower[(index+int(num))%26]
            elif value.isupper():
                for index,val in enumerate(upper):
                    if value == val: newstr += upper[(index+int(num))%26]
        else: newstr += value 
    return newstr

def caesar_dec(text, num):
    newstr = ""
    lower, upper = string.ascii_lowercase, string.ascii_uppercase
    for value in text:
        if value.isalpha():
            if value.islower():
                for index,val in enumerate(lower):
                    if value == val: newstr += lower[(index-int(num))%26]
            elif value.isupper():
                for index,val in enumerate(upper):
                    if value == val: newstr += upper[(index-int(num))%26]
        else: newstr += value 
    return newstr

while True:
    menu = input("Select 1 or 2 (1 is for encode; 2 is for decode): ")
    if menu.isdigit():
        if int(menu) == 1 or int(menu) == 2:
            break
    else:
        print("Select 1 or 2")
        continue

if int(menu) == 1:
    text_enc = input("Write down text for encode: ")
    while True:
        number_enc = input("Select a number for decode: ")
        if number_enc.isdigit():
            break
        else:
            print("Select number only")
            continue
    
    result_enc = caesar_enc(text_enc, number_enc)
    print(f"This is your encrypted version: {result_enc}")

elif int(menu) == 2:
    text_dec = input("Write down some text for decode: ")
    while True:
        number_dec = input("Select number for decode: ")
        if number_dec.isdigit():
            break
        else:
            print("Select number only")
            continue

    result_dec = caesar_dec(text_dec, number_dec)
    print(f"This is your decrypted version: {result_dec}")