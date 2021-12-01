# def unique(lists):
#     new = set(lists)
#     new_list = list(new)
#     print(new_list)

# unique([1,2,3,3,3,3,4,5])

def unique(lists):
    new = []
    for i in lists:
        if i not in new:
            new.append(i)
    print(new)

unique([1,2,3,3,3,3,4,5])
