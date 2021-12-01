def even_odd(lists):
    even_list = []
    odd_list = []
    even = 0
    odd = 0
    for i in range(len(lists)):
        if(lists[i] % 2 == 0):
            even_list.append(lists[i])
            even += 1
        else:
            odd_list.append(lists[i])
            odd += 1
    print(even_list)
    print(odd_list)
    print(even)
    print(odd)

even_odd([1,2,3,4,5,6,7])