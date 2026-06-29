
library =[] #list of dictionaries

while True: 

    print("===== Library App =====")
    print("1- Add Book")
    print("2- Show Books")
    print("3- Search Book")
    print("4- Exit")
    choice = input("\nEnter your choice from the menu :")

    # Add Book
    if choice == "1":
        title = input("Enter title of book :")
        author = input("Enter name of author : ")
        year = input("Enter year of this book : ")

        book ={ "title":title, "author":author, "year":year}
        library.append(book)

        print("Book added successfully! \n")
     
     #Show Books
    elif choice == "2":
        if len(library) == 0:
            print()
            print("The library is empty. Add a book to get started")
        else:
         print("\n===== Books =====")
         for i, book in enumerate(library):      # use enumerate() to show element and number of element   
            print()
            print(f"Book : {i+1}")
            print(f"Title : {book['title']}")
            print(f"Author : {book['author']}")
            print(f"Year : {book['year']}")
            print("----------------")

    # Search Book
    elif choice == "3":
        search_title = input("Enter book title to search: ").lower()

        found = False

        for book in library:
            if search_title in book["title"].lower():
                print("\nBook Found ")
                print(f"Title : {book['title']}")
                print(f"Author : {book['author']}")
                print(f"Year : {book['year']}")
                print("----------------")
                found = True
                
        if not found:
            print("\nBook not found\n")

    # Exit from the app
    elif choice == "4":
        break
    # if you dont enter the right syntax print  this warning / click enter to back the menu
    else:
     print(" \nInvalid choice, please enter 1-4 only")
     input("Press Enter to continue...") 


