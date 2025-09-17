def numbers( a,b):
    r=b*a
    return r
a = float(0.5)
b=float(0.7)
results= numbers(a,b)
print(results)
answer = input ( " what is your name ?")
print( "hello, "+ answer)
freind=  input (" what is your name ?")
print(f"hello,{freind}")
print("hello world",end="!\n")
z= int(input("x: "))
m= int(input("y: "))
print((z+m))
s= input("x: ")
z=input("y: ")
if s==z:
    print("they are the same")
else:
    print("different")
s= input(" Do you agree? ")
if s=="y"or s=="Y":
    print("Agree")
elif s=="n" or s=="N":
    print("Not agreed")
else:
    print("invalid")
d = input ( "do you agree").lower()
if d in [ "yes","y"]:
    print("Agreed")
elif d in ["n","no"]:
    print("Not agreed")
p= input("x:").capitalize()
print(p)
count=0
while count <3:
    print("meow")
    count+=1
for _ in range(3):# we can use the _ and the i to just present the character 
    print('meow')
before = input("After: ")
print('After:', end="")
for c in before:
    print(c .upper(),end="")
print()
# i can us ethe following code which is much way shorter 
before=input("after:")
after= print(f"After: {before.upper()}")
for _ in ["cat","bird","mouse"]:
    print('meow')
name = input("what is your name ")
print("hello,", end="")
print(name)
# remove the white space form the str, so this removes from both ends of the str, also we can choin the title function inside it 
name= name.strip().title()
print("hello ,",name)
# split the users name in to first name and last name 
first,last = name.split(" ")
print(last)
"""
anything between this is a comment .

"""
print('hello,"friend"')
print("hello, \"friend\"")
x= int(input("x:"))
y=int(input("y:"))
print(x+y)
#using the def function to create our very own functions
def hello(to="world"):
    print("hello", to)

# try some other ways 
def main():# first define the main function so that we wont make our code from botton upwards .
    name=input("what is your name")
    hello(name)
main()
#prrompt the user to enter int
def main():
    x=int(input('What is x: '))
    print(f'the square of {x} is',square(x))
def square(n):
    return pow(n,2)
main()




