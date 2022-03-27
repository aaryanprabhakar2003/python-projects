import pickle
print('''THIS IS STUDENT MANAGEMENT SYSTEM
1)CREATE YOUR USERNAME AND PASSWORD
2)LOGIN
3)EXIT''')
opt=int(input("Enter Your Choice="))
if opt==1:
    username=input("Enter Your Username=")
    password=input("Enter Your Passwrod=")
    user_data={username:password}
    f=open("userdata.dat","wb")
    pickle.dump(user_data,f)
    f.close()
if opt==2:
    username=input("Enter Your Username=")
    password=input("Enter Your Passwrod=")
    f=open("userdata.dat","rb")
    validation=pickle.load(f)
    user_data={username:password}
    if username not in  validation.keys():
        print("Incorrect Username")
    elif password not in validation.values():
        print("Incorrect Password")   
    else:
        print("Now You Are Logged In To Your Account")    
        print("1)ENTER DATA")
        print("2)UPDATE DATA")        
        print("3)DELETE DATA")         
        print("4)SEARCH FOR DATA") 
        option=int(input("Enter Your Choice="))
        if option==1:  
            def insertRec():
                rollno=int(input("Enter Roll No="))
                name=input("Enter Name=")
                marks=int(input("Enter Marks="))
                rec={"Rollno":rollno,"Name":name,"Marks":marks}
                f=open("student.dat","ab")
                pickle.dump(rec,f)
                f.close()
            #for i in range(3):
            insertRec()
        if option==4:   
            def searchRollNo():
                r=int(input("Enter Roll No Whose Data You Want To See="))
                f=open("student.dat","rb")
                while True:
                    try:
                        rec=pickle.load(f)
                        if rec["Rollno"]==r:
                            print("Record Found")
                            print("Roll No:",rec["Rollno"])
                            print("Name:",rec["Name"])
                            print("Marks:",rec["Marks"])
                            break
                    except EOFError:
                            print("No Record Found")
                            break
                f.close()
            searchRollNo() 
        if option==2:
            def updateMarks():
                r=int(input("Enter Roll No Whose Marks You Want To Update="))
                f=open("student.dat","rb")
                reclst=[]
                while True:
                    try:
                        rec=pickle.load(f)
                        reclst.append(rec)
                    except EOFError:
                         break
                f.close() 
                flag=False
                for i in range(len(reclst)):
                    if reclst[i]['Rollno']==r:
                        print("1 Record Matched")
                        m=int(input("Enter Marks="))
                        reclst[i]["Marks"]=m
                        flag=True
                    if flag==True:
                        f=open("student.dat","wb")
                        for k in reclst:
                            pickle.dump(k,f)
                        f.close() 
                    else:
                        print("No Record Found")
            updateMarks()      
        if option==3:    
            def delrecord():
                r=int(input("Enter Roll No Whose Record You Want To Delete="))
                f=open("student.dat","rb")
                dellist=[]
                while True:
                    try:
                        rec=pickle.load(f)
                        dellist.append(rec)
                        #print(dellist)
                    except EOFError:
                        break
                f.close() 
                flag=False
                for i in range(len(dellist)):
                    if dellist[i]['Rollno']==r:
                        print("Record Matched")
                        #print(dellist)
                        dellist.remove(dellist[i])
                        #print(dellist) 
                        flag=True
                    if flag==True:     
                        f=open("student.dat","wb")
                        for k in dellist:
                            pickle.dump(k,f)
                        f.close() 
                    else:
                        print("No Record Found")
            delrecord()    
if opt==3:
    print("Thanks For Using Our System!!!!")            
          
