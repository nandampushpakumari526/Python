print("--------------split bill----------------")
#normal
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
c=b/a #c=b//a
print("ecach per head=",c)
#f string
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
c=b/a #c=b//a
print(f"ecach per head={c}")
#formating string
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
c=b/a #c=b//a
print("ecach per head= {}".format(c))
#using functions
#method 1
def bill():
    a=int(input("enter the how many people u have"))
    b=int(input("enter the total value u have"))
    c=b//a
    return c
print(bill())
#method 2
def bill():
    a=int(input("enter the how many people u have"))
    b=int(input("enter the total value u have"))
    c=b/a
    print("ecach per head=",c)
bill()
#method 3
def bill(a,b):
    c=b//a
    print("ecach per head=",c)
a=int(input("enter the how many people u have"))
b=int(input("enter the total value u have"))
bill(a,b)
