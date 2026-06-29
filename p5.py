# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

family1 = {
    "father":"ali",
      "son": "moham"
}

family2 ={
    "father":"iop",
    "son":"vir"
}

allfamily = {"family1":{"father":"ali",
                        "son":"moham" , "phone":"078954321"},
                        "family2":{"father":"ibrahim",
                                   "son":"rashed", "phone":"7799"}}

print(allfamily["family2"]["son"])

#print(family1.items())

for key,value in family1.items():
    print(key)

for k, v in allfamily.items():
    print(k,v)
for v in v.values():
    if v == "rashed":
        continue
    print(v)

def hello():
    print("ff")
hello()


# no output
def hello(): 
    pass
"""
a = float(input("enter the f num:"))
b = float(input("enter the s num:"))
c = float(input("enter the th num:"))

# round تقريب الى اقرب منزلتين لبعد الفاصلة 
def avg (a=1,b=3,c=6):# local 
    s=(a+b+c)/3
    print(round(s,2))# globaly variable
avg()
print(round(5.3))
"""

l=[3,5,6]
def average(li):
    sum=0
    for i in li:
        sum+=i
    avg = sum/len(li)
    return avg
print(average(l))

"""
l =[]
while True:
    x  = input("enter the num or type q to exit: ")
    if x.lower() == "q":
        break
    x=float(x)
    sum = 0
    for i in l:
        sum+=i
    l.append(x)
    avg=sum/len(l)
print(l)
print(avg)
"""

##############################3333
l=[3,5,8,9]
print(l)# لليست عادية
print(*l)#unbacking بجردها او بخلصها من الالليست

def average (*li):
    sum=0
    for i in li:
        sum+=i
    avg= sum/len(li)
    return avg
print(average(1,2,3,4,5))

x=5
z=1
for i in range(x,0,-1):
    if i == 1:
        continue
    z *=i
    print(z)
print(z)

hello =lambda name: f"hello {name}"
hello("shaimaa")

#obj take from the class

#oop
# function is method
class Member:# member11 is a obj
    user_num = 0
    def __init__(self,firstname,lastname):
      self.__fname = firstname # private __fname
      self.lname = lastname # public
      Member.user_num+= 1
    def get_fname(self):#getter
        return f"hello your first name is {self.__fname} and your lastname is {self.lname}"
    
    def set_name(self,new_fname):# setter
        self.__fname = new_fname
        return new_fname
  
firststudent = Member("shaimaa","bataineh")
secondstudent = Member("ss","bb")
third = Member("aya","talfah")

#print(firststudent.__fname) # private error لايمكن الوصول لل برايفت الا باستخدام ال قيتر او من داخل الكلاس 
#print(firststudent.lname)
print(firststudent.get_fname())
print(secondstudent.get_fname())
#print(Member.user_num)
firststudent.set_name("ayat")

#print(firststudent.fname)

#print(secondstudent.fname)
#firststudent.set_name()
print(firststudent.get_fname())
#private  / public


class Food :
    def __init__(self,name):
        self.name = name 
        print("this is base class")
    def eat(self):
        print(f"{self.name} is food method")
class Fruit(Food):
    def __init__(self,name):
        self.name = name
        print("this is fruit class")
fries = Food("widges")
fries.name
fries.eat()

apple = Fruit("green apple")
apple.name
apple.eat()

# magic method / polymorphsim / static / class dicroters 



