from string import ascii_letters , digits

def change_case(orig_string: str):
    result=""
    for i in range(len(orig_string)):
        if orig_string[i].isupper():
            result += orig_string[i].lower()
        else:
            result += orig_string[i].upper()
    return result


def split_in_half(orig_string: str):
    div_index = len(orig_string)//2
    return (orig_string[0:div_index],orig_string[div_index:])

def remove_special_characters(orig_string: str):
    result=""
    for elements in orig_string:
        if elements in ascii_letters or elements in digits or elements == " ":
            result += elements
    return result




