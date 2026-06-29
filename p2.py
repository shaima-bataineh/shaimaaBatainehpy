
name = "shaimaa jamal bataineh"

P= name.title()
print(P)
U=name.capitalize() # تحول اول حرف فقط الى كبيتل 
print(U)
print(name.count("a"))

print(len(name)) # str هي سلسة كل حلقة فيها عبارة عن كركتر

#index
print(name[4])
print(name[-1])
print(name[15])
print(name[7:16]) # لازم نضيف في النهاية واحد حتى لو عدد 15 ضفت 16

print(name[7:])
print(name[:])
print(name[0:15:2])
print(name[-16:])
print(name[-7:])
print(name[-1::-1])
print(name[-3:-8:-1])
print(name.find("h")) # بيظهرلي موقع الحرف 
print(name.replace("a","A"))

x =name.split()# outputlist 

print(x)

print(type(x))
print(x[0])
print(x[2])
print(x[0:])
y = " ".join(x)
print(y)

n = " ".join(name)
print(n)

print(name.lower())
print(name.upper())
names = ["sh","th","ay"]
print(names)

names.append("sha")
print(names)
names.insert(0,"sos")
#print(names)

num = [1,2,3,4]
list1 = names[:]
list1.extend(num)
print(names)
print(list1)
age =[22,24,25,21,19]
age.sort(reverse=False)
print(age)


names ="As a result of the examples above, the lists will now contain 4 items."

print(len(names))
t = names.split()
print(names.count(" "))

#n = input("enter your name : ")
#print("hi, " + n)

#a = int(input("enter year:"))

#age =2026 -a
#print("my year of birth is : " +  str(age))

text ="Sublime Text can now utilize your GPU on Linux, Mac and Windows when rendering the interface. This results in a fluid UI all the way up to 8K resolutions, all while using less power than before"

word = len(text)
w1 = text.split(".")

sen = text.count(".")+ text.count(",") 
print(word)
print(w1)
print(sen)
