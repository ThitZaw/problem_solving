import re

def split_text(input_str):
    new_str = input_str[0].lower()
    for letter in input_str[1:]:
        if letter.isalpha():
            if letter.islower():
                new_str += letter.lower()
            else:
                new_str += " "
                new_str += letter.lower()
    return new_str
        
def combine_text(mcv,input_str):
    new_str = input_str[0].upper() if mcv == "C" else input_str[0].lower()
    flags = "lower"
    for letter in input_str[1:]:
        if letter == " ":
            flags = "upper"
            continue
        if flags == "upper":
            new_str += letter.upper()
            flags = "lower"
        else:
            new_str += letter.lower()
            
    if mcv == "M":
        new_method_txt = new_str.rstrip() + "()"
        return new_method_txt
        
    return new_str
    
    
    
while True:
    try:
        input_str = input().rsplit(';')
        if input_str[0] == "":
            break
        elif input_str[0] == "S":
            print(split_text(input_str[2]))
        elif input_str[0] == "C":
            print(combine_text(input_str[1],input_str[2]))
    except Exception as e:
        break