
print("MY \nname is \n Shivam")
print("MY \'name' is \t Shivam")
print("MY  \"name\" is \t Shivam")
# Calculator
a=int(input("enter first number: "))
b=int(input("enter second number: "))
print(f"Addition of numbers is",a+b)
print(f"substraction of numbers is",a-b)
print(f"Multiplication of numbers is",a*b)
print(f"Division of numbers is",a/b)
print(f"quotent of numbers is",a//b)

name="Shivam"
print(name)
name=123
name+=1
print(name)

firstname="Shivam"
lastname="Raj"
print(firstname+" "+lastname)
print(firstname*7)

name=input("please enter your name : ",)
print("hello " + name)
age=int(input("please enter your age:"))
print("your age is:"+ str(age))

n=input("Enter your name: ")
age=int(input("Your age: "))
print("your name is "+ n + " and you are "+str(age)+" old")

# split function
name,age=input("your name and age seperated by inverted commas :").split(",")
print("Your name is "+name+" age is "+str(age))

name="Shivam"
age=18
print("hello {} you are {} year old ".format(name,age))
print(f"hello {name} and you are {age} year old")

num1,num2,num3=input("please enter your seperated by commas:").split(",")
print("average of your inserted numbers is:",(int(num1)+int(num2)+int(num3))/3)

n="Python"
print(n[5])
print(n[-1::-1])# to print string in reverse order
print(n[-5])
print(n[::2])
print(n[3::-2])

a=input("enter your name: ")
reverse=a[-1::-1]
print(f"reverse of your name is:{reverse}")

name="Shivam Raj"
print(name.lower())
print(name.upper())
print(name.title())
print(name.count("a"))
print(len(name))

name,char=input("enter your name and character seperated by comma:").split(",")
print(f"length of your name is{len(name)}")
print(f"characters in your name is{name.count(char)}")

name="   Shivam  Raj       "
dots="........................."
print(name+dots)
print(name.lstrip()+ dots)
print(name.rsplit())
print(name.split()+ dots)
print(name.replace(" ",""))

a="Shivam"
b=a.replace("k","K")
print(b)

a="Shivam"
a+="Raj"
print(a)

str="there was a boy he was naughty"
print(str.find("was"))
a=str.find('was')
b=str.find("was",a+1)
print(b)

name="Shivam"
print(name.center(13,"*"))

name=input("Enter your name here:")
print(name.center(len(name)+8,"*"))

# if condition
a=int(input("Enter any number here:"))
if a<15:
    print("less than")
elif a==15:
    print("equal to")
else:
    print("greater than")

# pass condition
a=15
if a<15:
    pass
print("True")

# and & or condition
a="abc"
b=123
if a=="abcd" or b==123: # if any of the condition matches then condition is true
    print("true")
else:
    print("False")

name="Shivam"
if 'i' in name:
    print("i is present in name")
else:
    print("i is not present in name")

n=input("Enter your name")
if n:
    print(f"Your name is present in n {n}")
else:
    print("you have not written anything")

# while loop
sum=0
i=1
while i<10:
    sum+=1
    i+=1
    print(sum)
# finding the total number in string
number=input("enter a number: ")
sum = 0
i = 0
while i < len(number):
    sum += int(number[i])
    i += 1
print(sum)
