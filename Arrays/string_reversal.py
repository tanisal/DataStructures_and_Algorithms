#Reverse String
def reverse_str(words):
    if not isinstance(words,str):
        raise ValueError("Add a string please!")
    return words[::-1]
