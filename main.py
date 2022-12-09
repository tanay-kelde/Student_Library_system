class library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayAvailablebooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print("*" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}. please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True 
        else:
            print("sorry, this book is either not available or has already been issued to someone else. please wait until the book is available.")
            return False 
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book ! hope you enjoyed reading it.Have a great day!")

class Student:
    def requestBook(self):
        self.Book = input("Enter the name book you want to borrow: ")
        return self.Book

    def returnBook(self):
        self.Book = input("Enter the name book you want to return: ")
        return self.Book

if __name__ == "__main__":
    centrallibrary = library(["algoritham" ,"database" ,"django" ,"clrs" ,"flask"])
    Student = Student()
    # centrallibrary.displayAvailablebooks()
    while(True):
        welcomeMsg = '''\n === welcome to centrallibrary ===
        please choose an option :
        1. List of the books 
        2. request of books
        3. Add/return a books 
        4. exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice : "))
        if a == 1:
            centrallibrary.displayAvailablebooks()
        elif a == 2:
            centrallibrary.borrowBook(Student.requestBook())
        elif a == 3:
            centrallibrary.returnBook(Student.returnBook())
        elif a == 4:
            print("Thanks for choosing central library.  Have a great day ahead!")
            exit()
        else:
            print("Envlid choice!")
        
       