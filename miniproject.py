name = input("enter your name :")
age = int(input("enter your age :"))
major = input("enter your major : ")
mark = float(input("enter your mark : "))

students = {
    "names":[],
    "ages":[],
    "majors":[],
    "marks": []
}

students["names"].append(name)
students["ages"].append(age)
students["majors"].append(major)
students["marks"].append(mark)
print(students)

for i in range(len(students["names"])):
    print(f"student {i+1}")
    print("Name : ",students["names"][i])
    print("Age : " ,students["ages"][i])
    print("Major : ",students["majors"][i])
    print("Mark : ",students["marks"][i])
