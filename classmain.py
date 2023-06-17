# #START

# class User:
#     pass
# user1=User() 
# #here user1 is a instance or object of class User.
# user1.first_name="Manoj"
# user1.last_name="Pun"
# #To attach data to object, we first type the name of object,a dot,a name of the variable and give it a value.
# #Here in line 5 and 6,first_name and last_name we call it attributes/field and "Manoj" and "Pun" is data.
# print(user1.first_name,user1.last_name)

# first_name="Hari"
# last_name="Magar"
# print(first_name,last_name)
# #In classes even though we use the same variable names the values are kept separate.

# user2=User()
# user2.first_name="Ram"
# user2.last_name="Gurung"
# print(user2.first_name,user2.last_name)
# #In classes there no limit to number of objects you can make.
# #So basically classes are used to make objects, and each objects can have different values for the same variable names.

# user1.age=67
# user2.favourite_book="2000:A Space Odyssey"
# print(user1.age,user2.favourite_book)
# #You can add additional fields to the objects for the same variable names.
# # You can add additional fields to objects and they do not have to be string

# #FINISH

# #START
# class Item:
#     pass
# user2=Item()
# user2.first_name="Manoj"
# user2.last_name="Pun"
# #The 37 line of the code adds a first_name attribute to user2 and sets it to "Manoj", 
# # and the 38 line adds a last_name attribute to user2 and sets it to "Pun".
# #  These attributes are added to the user2 object specifically, not to the Item class in general.
# print(user2.first_name,user2.last_name)
# #The 42 line of the code prints the first_name and last_name attributes of user2 using the print() function. 
# # This should output "Manoj Pun" since those are the values that were assigned to user2.first_name and user2.last_name.
# # It's worth noting that the Item class itself does not have any attributes or methods, 
# # and so user2 is just an instance of this empty class with two extra attributes added to it.

# #FINISH

# #START

# # class Student:
# #     list=[]
# #     def addstudent(self,name,roll,subject):
# #         self.list.append({"name":name,"roll":roll,"subject":subject})
# #     def display(self):
# #         print(self.list)
# # obj=Student()
# # obj.addstudent("manoj",1,"science")
# # obj.addstudent("adarsh",1,"science")
# # obj.addstudent("dura",1,"science")
# # obj.display()

# #FINISH


# #START

# class StudentRecord:
#     studentlist=[]
#     def add_student(self,name,gender,dob,roll,address,adfee):
#         self.studentlist.append({"name":name,"gender":gender,"dob":dob,"roll":roll,"address":address,"adfee":adfee})
#     def display(self):
#         print(self.studentlist)
#     def count_gender(self):
#         cm=0
#         cf=0
#         for gender in self.studentlist:
#             # print(gender)
#             if gender["gender"]=="male":
#                 cm+=1
#             elif gender["gender"]=="female":
#                 cf+=1
#         print(f"The number of male is {cm} and number of female is {cf}")
#             # print(gender["gender"])
#     def total_money(self):
#         total_money=0
#         for money in self.studentlist:
#             # print(money)
#             total_money+=money["adfee"]
#         print(f"The total money collected is {total_money}")
#     def search_student(self,name):
#         for studentname in self.studentlist:
#             # print(studentname['name'])
#             # new_name.append(studentname['name'])
#             if name in studentname['name']:
#                 print(studentname)
#                 break
#             else:
#                  pass
#             # record.append(studentname)
#         # if name in new_name:
#         #     print(record)
#         # else:
#         #     print("NOT FOUND")
#             # if studentname["name"]=='Adarsh':
#             #     print(studentname)
#             #     break
#             # else:
#             #     print("Result not found")
#             #     break

# obj=StudentRecord()

# obj.add_student("Manoj","male","2061-05-31",1,"Tokha",20000)
# obj.add_student("Adarsh","male","2061-03-31",1,"BAgbaxar",20000)
# obj.add_student("Sita","female","2061-07-31",1,"Tdhfgdf",20000)
# obj.add_student("Gita","female","2061-01-31",1,"Tgsdfg",20000)
# obj.add_student("Meera","female","2061-06-31",1,"Tghsdfg",20000)
# # obj.display()
# # obj.count_gender()
# # obj.total_money()
# # obj.search_student('Adarsh')

# while True:

#     print("1. Add Student")
#     print("2.Display Student")
#     print("3.Gender Count")
#     print("4.Total money collected")
#     print("5.Search Student")



#     choice=int(input("Enter your choices:"))

#     if choice==1:
#         name=input("Enter the name:")
#         gender=input("Enter the gender:")
#         if gender!="male" or gender!="female":
#              pass
#         else:
#              print("Only male and female")
#         dob=input("Enter the dob:")
#         roll=int(input("Enter the roll:"))
#         address=input("Enter the adress:")
#         adfee=int(input("Enter the admission fee:"))
#         obj.add_student(name,gender,dob,roll,address,adfee)

#     elif choice==2:
#             obj.display()
#     elif choice==3:
#             obj.count_gender()
#     elif choice==4:
#             obj.total_money()
#     elif choice==5:
#             search=input("Enter the name to search:")
#             obj.search_student(search)
#     elif choice==0:
#          break
#     else:
#         print("Option doesnt match")

# #FINSIH

#START

# class Student:
#      school="THE MANOJ"
#      #IF you create a variable inside a class then it is called class attributes.
#      #Here school is a class attribute.
#      def __init__(self,full_name,course):
#           #Here self is a default arguments that is reference to the new object that is being created.
#           self.name=full_name
#         #   print(self.name)
#           #Here we stored values to fields in the object.
#           #.name is a field and full_name is a value/data.
#           self.course=course
#           #Here note:course is a value whereas .course is a field that stores the value.
#     #if you create a function within class then that function is called method.
#     #And if you create a variable inside that function then those variables are called instance attributes.
#     #Here name and course are instance attributes.
# Student1=Student("Manoj Pun","Javascript")
# print(Student1.school)
# Student2=Student("Ram Magar","Python")
# print(Student1.name)
# print(Student2.course)

#FINISH



#START

#Core concept of classes
class Person:
    def __init__(self,full_name):
        self.name=full_name
        #self references the current object.
    def talk(self):
        print(f"Hi,I am {self.name}") 
object=Person("Manoj")
object.talk()
object.name="Manoj"
print(object.name)

#FINISH


# #START
# #Why use constructor(_init_)??
# #-->Because it runs itself without calling it.Like,
# class Python:
#     def __init__(self):
#         print("This is constructor.")
# object=Python()
# #But it acts only for print function.

# #Also because it makes code shorter.Like
# class Shorter:
#     def name(self,full_name):
#         self.name=full_name
#     def course(self,course):
#         self.course=course
# code=Shorter()
# code.name("Manoj Pun")
# code.course("Python")
# print(code.name,code.course)

# #Now the above code could be written in shorter by using init
# class Shorter:
#     def __init__(self,full_name,course):
#         self.name=full_name
#         self.course=course
# code=Shorter("Manoj Pun","Python")
# #Since there is no print function it wont be called itself.So we have to print it.
# print(code.name,code.course)

# #FINISH

# #START 
# #MORE ON init
# class Employee:
#     def __init__(self,name,age,salary,gender):
#         self.full_name=name
#         self.age=age
#         self.salary=salary
#         self.gender=gender
#     def employee_details(self):
#         print(f"My name is {self.full_name}")
#         print(f"My age is {self.age}")
#         print(f"My salary is {self.salary}")
#         print(f"My gender is {self.gender}")
# object=Employee("Manoj Pun",18,20000,"male")
# object.employee_details()
# #FINISH


gdfjkg