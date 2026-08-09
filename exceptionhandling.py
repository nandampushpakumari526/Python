#exception handling
#syntax error
'''for i in range(20)
print(i)-----> here rise the syntax error'''
#run_time error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)#10//0->zero divisition error'''
#logical error
'''a=10
b=20
print(a-b)'''
#exception handling
'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exception")
    finally:
        print("program ends.....")'''
#file handling
#write()
'''a=open("pooja.text","w")
b=a.write("python fill stack")
a.close()'''
'''a=open("pooja.text","w")
b=a.write("pushpa kumari")
a.close()'''
#append()
'''a=open("pooja.text","a")
b=a.write("\tfrom mangalagiri")
a.close()'''
'''s=input()
a=open("pooja.text","a")
b=a.write(s)
a.close()'''

'''a=open("pooja.text","w")
b=a.write(input("data"))
a.close()'''
'''a=open("pooja.text","w")
b=input("data")
b=a.write(b)
a.close()'''
#read()
#a=open("pooja.text")
#print(a.read())#it will display entire content
#print(a.readline())#it will display first line
#print(a.readlines())#it will display in list with \n
#print(a.read(7))#it will display no.of characters


#writelines()->it makes every object side by side
'''a=open("pushpa.text","w")
b=["pushpa","teja","devi","prasanth","bharani"]
a.writelines("\n".join(b))
a.close()'''
'''a=open("dict.py")
print(a.read())'''
'''a=open("D:\pfs-38\python38\dict.py")
print(a.read())'''


