#loops in python

#while loop
print("printing hello world by using while loop")
a = 1
while(a < 10):
    a = a + 1
    print("hello world")

#for loop
print("printing hello world by using for loop")
for i in range(1,11):
    print("hello world")

#print tables
num = int(input("enter the number: "))
print("table by using while loop")

a = 1
while(a < 10):
    a = a + 1
    print(f"{num} X {a} = {num * a}")

print("table by using for loop")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
