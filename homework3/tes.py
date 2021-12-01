# def x(a,b):
#     def y(c,d):
#         return c + d
    
#     return y(a, b)
#     return a
# result = x(5,10)
# print(result)

# def x(name, age = 20):
#     print(name,age)

# x('y',3)

# def add(a,b):
#     return a+5, b+5
# result = add(3,2)
# print(result)

# def x(num):
#     return num + 25
# x(5)
# print(num)

# def x(*args):
#     for i in args:
#         print(i)

# x(name="Emma", age="35")

# name="a"
# def x(param):
#     value = "a"
#     value = param
#     print(value)

# x('second')

def pow(b,p):
    y = b ** p
    return y
def square(x):
    a = pow(x,2)
    return a
n = 5
result = square(n)
print(result)
