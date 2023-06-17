# what is function? --> Function is a block of code which only runs when it is called

#  Types of function
# 1.built-in function:print(),input(),type(),len(), etc. 
# 2.user-defined function:function which is created by user. 

# Rules for creating function:
#  1.function name should be meaningful
# 2.function name should not be same as built-in function name.
# 3.function name should not be same as variable name.
# 4.function name should not same as keyword
# 5.function name should not start with number.
# 6.function name should not contain special character except underscore(_)

#declaration of function:
# def message():
#     print("Hello world")
#calling of function:
# message()
# message()

#function with parameter
# def message(name):
#     print("Hello",name)
# message("Manoj")
# message("Pun")

# def students(id,name,email):
#     print("Id:",id)
#     print("Name:",name)
#     print("E-mail:",email)
# students(1,"Manoj","Manojpun12@gmail.com")

#Function with optional parameter
# def user(name,age=0):
#     print("Name:",name)
#     print("Age:",age)
# user("Manoj")

# def user(name,age=0): Note:optional should be assigned from second and rest but not in the first like you cannot make name="Manoj"
#     print("Name:",name) Note:also like if you create optional then you have to create optional for the rest as well like age=0,address="Kathmandu"
#     print("Age:",age)
# user("Manoj",50)


# def users(*names):
#     print(names)
# users("Rahul","Manoj","Pun")
#either
# def users(names):
#     print(names)
# users(["Rahul","Manoj","Pun"])

# def users(*args,**kwargs): Kwargs-->keywords argument
#     print(args)
#     print(kwargs)
# users("Rahul","Raj","Ravi","Ramesh",name="Manoj",age=20,address="Kathmandu")

#Function return value
# def add(a,b):
#     return a+b
# print(add(30,5)) -->but this is best
#either
# def add(a,b):
#     return a+b
# result=add(30,5)
# print(result)

# default arguments
# def add(a,b=5): -->here b=5 is default arguments
#     return a+b
# print(add(30))

# def add(a,b):
#      a+b
# print(add(30,5))

# def add(a,b):
#     return a+b
#     return a-b -->this means you cannot give two return
# print(add(30,5))

# def add_sub(x,y):
#     a=x+y
#     b=x-y
#     return[a,b]
# res=add_sub(30,5)
# print(res)    

#Function Scope:
#global variable
#local variable

# x=10    -->this is called global variable
# def test():
#     print(x)
# test()

# but you cannot do the following:
# def test():
#     x=10
# test()
# print(x)

# x=10
# def test():
#     x=50
#     print(x)
# test()
# print(x)

# x=10
# def test():
#     a=x+10
#     print(a)
# test()

# x=10
# def test():
#     x=x+10
#     print(x)
# test()      -->here python does not understand x whether it is global or local so to solve that problem do the following

# x=10
# def test():
#     global x
#     x=x+10
#     print(x)
# test()
# print(x)

#Nested function
# def test():
#     print("Hello World")
# def message():
#     test()
# message()

# def students():
#     def home():
#         print("Hello ghar")
#     return home
# students()

#Lambda function
# a=lambda x,y:x+y
# print(a(10,20))

#mathiko ma vako chai yo ho
# def a(x,y):
#     return x+y

# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(5))

# def a():
#     return 10
# def b():
#     c=a()
#     print(c)
# b()




