def increment(x):
    x = x+1
    return(x)

def decrement(x):
    x = x-1
    return(x)


x = 1
print(x)
if x==1:
    print("X equals one")
else:
    print("X is not equal to one")
x = increment(x)
print("Now, x equals",x)