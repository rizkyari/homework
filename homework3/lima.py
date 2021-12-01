# def count_word(list):
#     lower = 0
#     upper = 0
#     for i in range(len(list)):
#         if(list[i] >='a' and list[i] <= 'z'):
#             lower += 1

#         elif(list[i] >='A' and list[i] <= 'Z'):
#             upper += 1
#     print(lower)
#     print(upper)

# count_word("DigiSkola")

# def count_word(list):
#     lower = 0
#     upper = 0
#     for i in list:
#         if(i.islower()):
#             lower +=1
#         elif(i.isupper()):
#             upper += 1
#     print(lower)
#     print(upper)

# count_word("DigiSkola")

s = "Hello World"
l,u = 0,0
for i in s:
    if (i>='a'and i<='z'):
        l=l+1                 
    if (i>='A'and i<='Z'):
        u=u+1   
          
print('Lower case characters: ',l)
print('Upper case characters: ',u)