#Create a calculator with +,-,*,/,//,% (whatever data types are in, this calculator must calculate it)

def add(a,b):
    int_a = int(a)
    int_b = int(b)
    return(int_a+int_b)
def sub(a,b):
    int_a = int(a)
    int_b = int(b)
    return(int_a-int_b)
def mul(a,b):
    int_a = int(a)
    int_b = int(b)
    return(int_a*int_b)
def quo(a,b):
    int_a = int(a)
    int_b = int(b)
    return(int_a/int_b)
def floored(a,b):
    int_a = int(a)
    int_b = int(b)
    return(int_a//int_b)
def remain(a,b):
    int_a = int(a)
    int_b = int(b)
    return(int_a%int_b)

print(add(3,4))
print(remain("3",7))
print(mul("45","5"))

#conditional part       if ~ elif ~ else

def remain(a,b):
    if type(a) is str:
        return None
    else:
        return a%b

print(remain("3",7))

def age_check(age):
    print(f"your age : {age}")
    if age < 18:
        print("you cant drink")
    elif 18 <= age and age < 30:
        print("drink")
    else:
        print("you are grounded")

age_check(21)



