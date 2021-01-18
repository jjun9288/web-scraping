#list
days = "Mon,Tue,Wed,Thur,Fri"
print(days) #It works but we can't print particular day like Wednesday.

days = ["Mon","Tue","Wed","Thur","Fri"]
print(type(days))
print(days[2])  #Now we can print particular day by using list.
#X in a
print("Mon" in days)    #return True or False.
#append,remove,pop,reverse,
days.append("Sat")
print(days)

#tuple  - Same as a list, but you cant change tuples. (No append,pop but still can use length,min,max,etc)
days = ("Mon","Tue","Wed","Thur","Fri")
print(type(days))

#dictionary
name = "Jun"
age = 27
Korean = True
Food = ["pizza","steak"]    #They are not in one place together. They are just a simple variables, so we can use dict for this.

Jun = {
    "name" : "Jun",    
    "age" : 27,
    "Korean" : True,
    "Food" : ["pizza","steak"]
    }
print(Jun)

#Interesting part about Python is that we can put different variables in list,tuple,or dict!