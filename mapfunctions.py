#map():

#map function using with lenght:
#lenght = ["i am srikamth", "from guntur", "working on a python developer"]
#l2 = list(map(len,lenght))
#print(l2)


#using map with lambda functions:
#num = (2,3,4,5)

#l2 = set(map(lambda i:i+i, num))
#print(l2)


#using map iterate:

#def iterate(n):
 #   return n

#list_1 =("this is srikanth")
#update_1 = list(map(iterate,list_1))
#print(update_1)


#map with tuple:
#def tuple_1(s):
    #return s.upper()

#list_1 = ("this","is","srikanth")
#list_2 = list(map(tuple_1,list_1))
#print(list_2)


#map function in dict:

#dict_1 = {"a":"srikanth","b":"guntur","c":"hyderabad"}

#dict_1 = dict(map(lambda x :(x[0],x[1]+"_"),dict_1.items()))
#print(dict_1)


#set using map():

#def set_1(n):
 #   return n*n

#set_3 = (1,2,3,4,5,6,7,8,9)
#output = set(map(set_1,set_3))
#print(output)


#def squre(name):
 #   return name * 23

#title = ["srikanth"]
#title_1 = list(map(squre,title))
#print(title_1)


#reduce function 
#from functools import reduce

#def my_red(a,b):
 #   return a *b


#list_1 = [1,2,3,4,5]
#print(reduce(my_red,list_1))


#reduce using lambda function:
#from functools import reduce 

#result = 1,2,3,4,5 
#output = reduce(lambda x,y:x+y,result)
#print(output)


#reduce function using function:
from functools import reduce

#def add(a,b):
 #   return a * b


#t = 1,2,3,4,5 
#t1 = reduce(add,t)
#print(t1)


#using lambda with more initilizations:
#from functools import reduce
#def more_1(a,b):
 #   return a + b

#result = reduce(more_1,[1,2,3,4])
#print(result)

#from functools import reduce

#result = reduce(lambda a,b:a + b, [1,2,3,4]) 
#print(result)



#filters:
#def filter_1(letter):
 #   list_of = ["a","e","i","o","u"]
  #  if letter in list_of:
   #     return True
    #else:
     #   return False 
#letter = ["s","r","i","k","a","n","t","h"]
#print(list((filter(filter_1,letter))))

#filter using lambda:
#list_1 = [1,2,3,4,5,6,7,8,9]

#l = filter(lambda i: i % 2 == 0,list_1)
#l1 = filter(lambda i:i % 2 == 1,list_1)
#print(list(l))
#print(list(l1))


def name(x):
    return x % 3 == 0
numbers = [1,2,3,4,5,6,7,8]
result = list(filter(lambda x:name(x),numbers))
print(result)




#nested functions:
#def fun1():
 #   print("this fun1")
  # def fun2():
   #     print("this is fun2")
    #fun2()
#fun1() 


#def add(a):
 #   def multiplier(b):
  #      return a * b 
   # return multiplier


#mul1 = add(3)

#mul2 = add(2)

#print(mul1(3))
#print(mul2(4))
#print(mul2(mul1(2)))
#
#def num(x):
 #   def no(y):
  #      return x + y 
   # return no
#print(num(2)(3))

#def greeting(first,last):
 #   def greet():
  #      return first + " " + last 
   # print("hi " +greet() + "!")
#print(greeting("mallela","srikanth"))