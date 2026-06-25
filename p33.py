# flask  / sql lat


"""
import math

l=[0,2,3,4,5,6,78,9]
print(max(l))
print(min(l))

print(round(2.6))
print(round(2.5))

print(math.floor(2.96))
print(math.ceil(2.9))

x =math.pi

print(round(x,2))

y= math.pow(2,4)# (#,#)

print(y)

r = float(input("enter the area :"))
area = math.pi * math.pow(r,2) # 3.14 * 6 **2 = 113.0

print("the area of the circle :", str(area))

t = 3.14 * 16.0
print(t)
"""
#  if /for 

print(4<7)
print(5==3)
print(5 >= 2)
print(5!=3)
print("5" == 5)

"""
x = int(input("enter the number : "))

if x > 9 :
    print(f"{x} is postive")

elif x < 0:
    print(f"{x} is negative")
else:
    print("zero is positive")


x =int(input("enter the number : ")) 
if x %2 == 0 :
    print(f"{x} is even")

elif x % 2 !=0 :
    print(f"{x} is odd")
else:
    print("enter the rgit number")

mark = float(input("enter the mark :"))
if mark >= 80 and mark <= 100:
    print(f"{mark} your mark is Exellent ")
elif mark >= 60 and mark < 80 :
        print(f"{mark} your mark is very good  ")

elif mark >= 50 and mark <60 :
        print(f"{mark} your mark is good ")

elif mark >= 0 and mark <50 :
        print(f"{mark} fail")

# shift + حرف الجيم
print(bool())# space == false

switch1 = int(input("enter the first switch state (1:on,0:off) :"))

switch2 = int(input("enter the first switch state (1:on,0:off) :"))

if switch1 and switch2 :
       print("on")
else:
       print("off")
#########################################################
switch1 = int(input("enter the first switch state (1:on,0:off) :"))

switch2 = int(input("enter the first switch state (1:on,0:off) :"))

if switch1 ==0 and switch2==1 :
       print("off")
elif switch1 ==0 and switch2==0:
       print("off")
elif switch1==1 and switch2==1 :
       print("on")
elif switch1==1 and switch2==0:
       print("off")
"""
for i in range (5): # i iteration to variable
       print("shaimaa")
for i in range(10,1,-1):
       print(i,"hello,world")

for i in "shaimaa bataineh":
       if i == "a":
              continue #بطبع كل شي الا حرف ال a
       if i== "i":
              break
       print(i,end="")
print(list(range(10)))
l= [1,3,5,8]
for i in range(len(l)):
       print(f"{i+1} th element is {l[i]}")

#homework
sum = 0
m=0
for i in range(5):
     n1=int(input("enter the number: "))
     sum+=n1
     if n1 > m :
       m = n1
avg = sum/5
print(f"total is {sum} ")
print("avg " + str(avg))
print(f"max is {m}")
  
       
