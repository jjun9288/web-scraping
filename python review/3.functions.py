#Built_in functions

#https://docs.python.org/3/library/functions.html?highlight=built
#type(), abs(), print(), len(), set(), etc are the built-in functions! Take a look at that link

#Create functions

def say_hello(who):    #Python doesn't work with {}. It works with identation.
    print("hello",who)

say_hello("Jun")    #need one arguement for 'who'

def plus(a,b=0):
    return a+b
    print(a+b)  #this print wont work because as soon as python returns, its done.

print(plus(2,3))
print(plus(2))     #no error even if we got one arguement because we have initial value for 'b'

def say_hello(name,age):
    return f"My name is {name} , age is {age}"  

hello1 = say_hello("Jun",12)
hello2 = say_hello(age=12,name="Jun")   #order is not important
print(hello1)
print(hello2)