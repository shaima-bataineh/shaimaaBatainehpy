students ={
    "names": [],
    "ages": [],
    "majors":[],
    "marks": []
}

while True :
    print("1- Add Student :")
    print("2- Show Students :")
    print("3- Search Student")
    print("4- Statistics :")
    print("5- Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
     name = input("enter your name :")
     age = int(input("enter your age :"))
     major = input("enter your major : ")
     mark = float(input("enter your mark : "))
     students["names"].append(name)
     students["ages"].append(age)
     students["majors"].append(major)
     students["marks"].append(mark)


    elif choice == "2":
       for i in range(len(students["names"])):
          print(f"student {i+1}")
          print(f"Name : {students["names"][i]}")
          print(f"Age : {students["ages"][i]}")
          print(f"Major : {students["majors"][i]}")
          print(f"Mark : {students["marks"][i]}")
          print("----------------------")


    elif choice == "3":
       search_n = input("enter the name you search for : ")
       found = False

       for i in range(len(students["names"])):
          if students["names"][i].strip().lower() == search_n.strip().lower():
             print("Student found :")
             print(f"Name : {students["names"][i]}")
             print(f"Age : {students["ages"][i]}")
             print(f"Major : {students["majors"][i]}")
             print(f"Mark : {students["marks"][i]}")
             found = True
             break
       if not found:
          
        print("student not found")
          
    elif choice == "4":
       if len(students["names"]) == 0:
          print("No student yet")

       else:
         
         print(f"Number of student : {len(students['names'])}")
         print(f"Hightes Marks : {max(students['marks'])}")
         print(f"Lowest Marks : {min(students["marks"])}")
         print(f"averge : {sum(students['marks'])/len(students['marks'])}")

         passed =[] 
         for mark in students["marks"]:
            if mark >= 50 :
               passed.append(mark)
            print(f"Passed student : {len(passed)}")
    elif choice == "5":
       break

