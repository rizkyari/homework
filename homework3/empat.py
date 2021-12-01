# def reverse_string(list):
#     x = list[::-1]
#     print(x)

# reverse_string("1234abcd")

def reverse_string(list):
    new_strings = []
    index = len(list)
    while index:
        index -= 1                       
        new_strings.append(list[index])
    print(new_strings)
    print (''.join(new_strings))

reverse_string("1234abcd")