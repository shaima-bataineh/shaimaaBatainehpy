#homework

sum = 0 # لو بحطها جوا الفور رح يعمل ريست 
m=0
for i in range(5):# 
     n1=int(input("enter the number: "))
     sum+=n1
     if n1 > m :
       m = n1
avg = sum/5
print(f"total is {sum} ")
print("avg " + str(avg))
print(f"max is {m}")

