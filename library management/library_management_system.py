import pickle
list_of_books=["Python","Programmin with C","Java Concepts"]
welcome=''' ****Welcome to Library Management System**** 
    Some important instructions to use automated library system:
       - Register yourself on portal first
       - Login with your credentials
       - Choose a book from list of books and get that book issued if it is available
       - Return book after reading the book '''
print(welcome)       
options='''Choose from options below:
       1. Register
       2. Login\n '''
while(True):
    options=input(options)
    if(options=='1'):
        username=input("Enter Username\n")
        password1=input("Enter Password\n")
        password2=input("Enter Password again\n")
        if password1==password2:
            user_db1={username:password1}
            f=open('reg.dat','rb')
            d=pickle.load(f)
            f.close()        
            if username in d.keys():
                    print("username already exists!!")
                    break
            else:   
                d.update(user_db1)
                f=open('reg.dat','wb')
                pickle.dump(d,f)
                f.close()
                print(f"updated dictionary: {d}")
                print("Registration Successful\nPress 1 for login\nPress 2 for exit")
                choice=input()
                if choice=='1':
                    username=input("Enter username\n")
                    password=input("Enter Password\n")
                    f=open('reg.dat','rb')
                    validate_data=pickle.load(f)
                    while(True):
                        if username not in validate_data.keys():
                            print("invalid username")
                            break
                        elif password not in validate_data.values():
                             print("invalid password")
                             break
                        else:
                            print("Login successful")
                            break
    else:
        username=input("Enter username\n")
        password=input("Enter Password\n")
        f=open('reg.dat','rb')
        validate_data=pickle.load(f)
    while(True):                    
        if username not in validate_data.keys():
            print("invalid username")
            break
        elif password not in validate_data.values():
            print("invalid password")
            break
        else:
            print("Login successful")
            print("Choose from options below:\n 1. Issue a Book\n 2. Return a Book")
            issue_return=input()
            if issue_return=='1':
                print("Choose from books: \n")
                for i in range(len(list_of_books)):
                    print(i+1," ",list_of_books[i])
                issue_book=int(input())
                f=open("booklist.dat","rb")
                r=pickle.load(f)
                f.close()
                print(list_of_books[issue_book-1]," book has been issued dont forget to return it within 15 days")
                break
            elif issue_return=='2':
                    list_of_books=["Python","Programmin with C","Java Concepts"]
                    h=input("Are you sure you want to continue to return book(y/n)")
                    if h=='y':
                        f=open('return.dat','rb')
                        r=pickle.load(f)
                        print(r)
                        issue_book=int(input("which book you want to return\n"))
                        if list_of_books[issue_book-1]:
                            print(list_of_books[issue_book-1],"book has been returned")
                            f=open("return.dat","wb")
                            r.remove(list_of_books[issue_book-1])
                            pickle.dump(r,f)
                            f.close()
                            a=["Python","Programmin with C","Java Concepts"]
                            f=open('return.dat','wb')
                            pickle.dump(a,f)
                    elif a=='n':
                        print("THANKS FOR USING LIBRARY MANAGEMENT SYSTEM")
                      

    

           





                
                        
            

           

            










# else:
#                f=open('booklist.dat','rb')
#                returnbook=pickle.load(f)
#                f.close()
#                if len(returnbook)==0:
#                    print("Please issue a book first. Thanks!")
#                    break
#                else:
#                    for book in list_of_books:
#                        if book not in returnbook:
#                            print("Return",book,"book?\nPress 'c' to confirm\nPress 'e' to exit\n")
#                            inp=input()
#                            if inp.lower()=='c':
#                                print("Thanks for returning",book,"\nPlease feel free to visit LMS to issue any book from library.")
#                                returnbook.append(book)
#                                f=open('booklist.dat','wb')
#                                pickle.dump(returnbook,f)
#                                f.close()
#                                break
#                            else:
#                                print("Thanks for using Library Management System.\nLogin again to issue or return a book")     
#                                break
#                       else:
#                           print("Our system has detected that no book has been issued, please issue a book first\n")
#                            break
#        break    
                    















































        
        
                   
                    

        
            
        
        
            


