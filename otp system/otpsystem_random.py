import random
import time
import pickle
print('''THIS IS A OTP  BASED LOGIN SYSTEM
WHICH OPTION YOU WANT TO PROCEED WITH:
1)SIGNUP
2)LOGIN
3)EXIT''')
option=int(input("PLEASE ENTER YOUR CHOICE="))
if option==1:
    username=input("ENTER YOUR USERNAME=")
    password=input("ENTER YOUR PASSWORD=")
    mobile_no=input("PLEASE ENTER YOUR MOBILE NO=") 
    if mobile_no.isdigit():
        if len(mobile_no)<10 or len(mobile_no)>10:
            print("PLEASE ENTER 10 DIGIT MOBILE NO")
    else:
        print("ONLY DIGITS ALLOWED")
    uid=random.randint(1111,9999)
    print(f"DEAR CUSTOMER YOUR UID LINKED WITH YOUR MOBILE NO {mobile_no} is {uid}")  
    password_dict={username:password}
    mobileno_dict={username:mobile_no}
    uid_dict={username:uid}
    #d[username]=[password,mobile_no,uid]
    local_time=time.ctime()
    print("USER REGISTERED AT ",local_time)
    #d[username]=[password,mobile_no,uid] 
    f=open("otp_system_password.dat","wb")
    pickle.dump(password_dict,f)
    f.close() 
    f=open("otp_system_password.dat","rb")
    output=pickle.load(f)
    #print(output)
    #f=open("otp_systemdata.dat","rb")
    #output=pickle.load(f)
    #print(output)
    #PASSWROD FILE
    f=open("otp_system_mobileno.dat","wb")
    pickle.dump(mobileno_dict,f)
    f.close()
    f=open("otp_system_mobileno.dat","rb")
    output1=pickle.load(f)
    #print(output1)
    f=open("otp_system_uid.dat","wb")
    pickle.dump(uid_dict,f)
    f.close()
    f=open("otp_system_uid.dat","rb")
    output2=pickle.load(f)
    #print(output2)
if option==2:
    username=input("ENTER YOUR USERNAME=")
    password=input("ENTER YOUR PASSWORD=")
    mobile_no=input("ENTER YOUR MOBILE NO=")
    uid=int(input("ENTER UID LINKED WITH YOUR MOBILE NO="))
    if mobile_no.isdigit():
        if len(mobile_no)<10 or len(mobile_no)>10:
            print("PLEASE ENTER 10 DIGIT MOBILE NO")
    else:
        print("ONLY DIGITS ALLOWED")
    #if uid.isdigit():
        #if len(uid)<4 or len(uid)>4:
           # print("PLEASE ENTER 4 DIGIT UID LINKED WITH YOUR MOBILE NUMBER")
    #else:
        #print("ONLY DIGITS ALLOWED")   
    f=open("otp_system_password.dat","rb")
    validation=pickle.load(f)
    #print(validation) 
    f=open("otp_system_mobileno.dat","rb") 
    validation2=pickle.load(f)
    #print(validation2) 
    f=open("otp_system_password.dat","rb") 
    validation1=pickle.load(f)
    #print(validation1) 
    f=open("otp_system_uid.dat","rb") 
    validation3=pickle.load(f)
    #print(validation3) 
    if username not in validation.keys():
        print(" PLEASE ENTER  CORRECT USERNAME")
    elif password not in validation1.values():
        print("ENTER CORRECT PASSWORD") 
    elif mobile_no not in validation2.values():
        print("ENTER CORRECT MOBILE NO")
    elif uid not in validation3.values():
        print("ENTER CORRECT UID WICH WAS SENT TO YOUR MOBILE NO")  
    else:
        local_time=time.ctime()
        print("YOU HAVE SUCCESSFULLY LOGGED IN TO YOUR ACCOUNT AT  ",local_time)
if option==3:
    print("THANKS FOR USING SYSTEM COME BACK LATER!!!!!!!!!!!")         
        

            
    
        


    
                