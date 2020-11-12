def increment(x):
    x = x+1
    print("add 1 to x")
    return(x)

def decrement(x):
    x = x-1
    print("subtract 1 from x")
    return(x)

print("Hi!  This is my VSCode tour")
x = 1
while x < 3:
    if x==1:
        print("x is equal to one")
    else:
        print("x is not equal to 1")
    x = increment(x)
    print("x is equal to",x)

