# class Student:
#     a=800
#     def __init__(self):
#         Student.a=400
#     def m1(self):
#         Student.c=500
#     @classmethod
#     def m2(cls):
#         Student.d=600
#         cls.e=1000

#     @staticmethod 
#     def m3():
#         Student.f=2000

# t=Student()
# t.m1()

# Student.a=666
# Student.f=999
# print(t.e)
# print(t.d)



#string dataype 

#pro to accept some string 
# from keyboard and print all the char with the index

# s=input("enter the string : ")
# print(len(s))
# i=0
# for x in s :
#     print("the char at +ve index is ",i,"and -Ve char is ",i-len(s),"is",x)
#     i+=1


# s="lenovo is a brand"
# # print(s[-4:-8:-1])
# # print(s[4:-15:-1])


# l1=["A","B","C"]
# l2=["A","B","C"]
# print(id(l1))
# print(id(l2))
# print(l1 is l2)#this will check the id of variables
# print(l1==l2)#will check the content

#swiggy & #zomato

# city=input("enter you city to check availability")#hyderabad
# zomato_list_cities=["hyderabad","vijayawada","guntur","tenali","bangolre"]
# if city.strip() in zomato_list_cities:
#     print("your",city," is available")
# else:
#     print("in this ",city,"will be available shortly ")
# print()


#lstrip()=> left hand side if it has spaces it removes
#rstrip()=right hand side 

#find()
#index()
#rfind()
#rindex()
# s="this is gopi and my name is gopi"
# # find(substring,start_index,end_index)
# print(s.find('gopi',14,20))
# print(s.find("aman"))#willl always return the first occurence of the index
# print(s.index("aman"))

# s=input("enter the string : ")#i like riding bikes 
# sub=input("enter the sub string : ")#riding 
# try:
#     n=s.index(sub)
# except ValueError:
#     print("sub string not found ")
# else:
#     print("sub string found in main string")


