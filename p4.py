"""
i =[1,2,3,4,6]
count =0
for i in i:
    print(f" element {count}: {i}")
    count +=1
"""

# enumerat
i =[1,2,3,4,6]
for index , elem in enumerate(i, start=1):
    print(f"index: {i}, value:{elem}")

"""
sum = 0

x = int(input("enter number: "))
mx = x
mn = x
sum = x

for i in range(4):
    x = int(input("enter number: "))
    sum += x

    if x > mx:
        mx = x

    if x < mn:
        mn = x

avg = sum / 5

print(f"sum is {sum}")
print(f"avg is {avg}")
print(f"max is {mx}")
print(f"min is {mn}")
"""
x=0
while True:
    x +=  1
    if x==6:
        continue
    if x==9:
        break# بكفي 
    print(x)
print("finished loop")

"""
sum=0
while True:
    x =input("enter number: ")
    if x=="stop":
        break
    sum += int(x)
print("the sum of the numbers is :", sum)


even =[]
odd =[]
while True:
    n=input("enter the number :")
    if x.lower() =="9":
        break
    num = int(n)
    if num % 2 ==0:
        even.append(num)
    else:
        odd.append(num)
print("even number :", even)
print("even number :", even)
"""

#tuple هي مجموعة عناصر غير قابلة للتغيير (immutable)
#Set items are unchangeable, but you can remove items and add new items.
days = ("Sun", "Mon", "Tue")
l = list(days)# convert list to tuple
print(l)
l[0]="th"
print(l)
days= tuple(l)
print(l)

s ={"b","h","u","p","h"}
print(s)
#تحذف المسافة strip()بس المسافة يلي قبل ويلي بعد تحذف
s="rty uit"
y = s.strip()
print(s)


l1 = [1, 2, 3, 4, 5, 1]
l2 = [3, 4, 1, 6, 7, 3]
l3 =[]
for i in l1:
    if i not in l2:
        l3.append(i)
for i in l2:
    if i not in l3:
        l3.append(i)
print(sorted(l3))
# for 2 شيكت مرتين على التبل 
#########################################################     
l1 = [1, 2, 3, 4, 5, 1]
l2 = [3, 4, 1, 6, 7, 3]

res = []
for i in l1 + l2:
    if i not in res:
        res.append(i)

print(res)
##########################################################
import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.year)

"""
birth_date = datetime.datetime(2003, 7, 6)  # حط تاريخ ميلادك الحقيقي
now = datetime.datetime.now()

age = now.year - birth_date.year
day_live = (now - birth_date).days
print(day_live)
# تصحيح إذا عيد الميلاد ما اجى هالسنة لسه
if (now.month, now.day) < (birth_date.month, birth_date.day):
    age -= 1

print(age)

birthday = int(input("enter your year birthday :"))
l = datetime.datetime.now()
age = now.year - birthday
print(age)

l1=[1,2,7,8,0,6,1]
l2=[1,88,0,56,4,32]
s1=set(l1)
s2=set(l2)
print(s1|(s2)) #union اتحاد 
# | = Pipe operator
# تقاطع 
print(s1-(s2))# difference 
"""
##################################################
myseries = {
    "name": "The Nun",
    "year": 2018,
    "rate": 5.4
}
myseries["year"]=2020
# set , dictonary / {} the same importent order , 
print(myseries["rate"])
print(myseries.values())
print(myseries.keys())
print(myseries.items()) #print into list[] of tuple()
for i in myseries:
    print(i)
# بقدر اطبع الكيز والايتم سوا 
student_dic = {
    "names": ["shaimaa", "kai", "shaden"],
    "age": [23, 22, 31],
    "degree": ["B.S", "m.s", "B.S"],
    "mark": [3.5, 3.2, 2.7],
    "major": ["BIT", "cs", "cis"]
}
print(student_dic)
for key, value in student_dic.items():
    print(key, value)

t =[1,2,3,6]
print(len(t))

