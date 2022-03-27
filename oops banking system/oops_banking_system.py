class Bank():
  def __init__(self):
    self.data=[]
    self.name=""
    self.age=""
    self.ph=""
    self.cash=0
  def register_system(self):
    conditions=True
    cash=self.cash
    name=input("Enter Your Name: ")
    age=int(input("Enter Your Age:"))
    ph=int(input("Enter Your Phone Number:"))
    if age<18:
      print("You Must Be 18 Years Old To Create Account")
      conditions=False
    if len(str(ph))>10 or len(str(ph))<10:
      print("Invalid Phone Number:")
      conditions==False
    if conditions==True:
        self.name=name
        self.age=age
        self.ph=ph
        self.data=[cash,name,age,ph]
        with open("bank_data.txt","w")as f:
          for data in self.data:
            f.write(str(data)+"\n")
          print("Registered Successfully")
  def login_system(self):
    with open("bank_data.txt","r")as f:
      data=f.read()
      self.data=data.split("\n")
      phone_number=int(input("Enter Your Phone Number: "))
      if str(phone_number) in str(self.data):
        print("Login Successfully")
        self.loggedin=True
      #if self.loggedin==True:
        #print("Login Successfully")
      else:
        print("Invalid Details")
  def add_cash(self):
    with open("bank_data.txt","r")as f:
      data=f.read()
      self.data=data.split("\n")
      cash=int(input("enter cash: "))
      with open("bank_data.txt","r+")as f:
        self.data=data.split("\n")
        self.data[0]=cash
        for data in self.data:
          f.write(str(data)+"\n")
        self.cash+=cash
        print("Amount Added")
      with open("bank_data.txt","r")as f:
        data=f.read()
        self.data=data.split("\n")
  def update_profile(self):
      with open("bank_data.txt","r")as f:
        data=f.read()
        self.data=data.split("\n")
      print('''What Do You Want To Update:
      1)Phone Number
      2)Name''')
      choice=int(input("Enter Your Choice:"))
      if choice==1:
          updated_phone_number=int(input("Enter Your New Phone Number: "))
          with open("bank_data.txt","r+")as f:
            self.data=data.split("\n")
            self.data[3]=updated_phone_number
            for data in self.data:
                f.write(str(data)+"\n")
            print("Your Phone Number Has Been Updated.")
      if choice==2:
          updated_name=input("Enter New Account Holder Name: ")
          with open("bank_data.txt","r+")as f:
            self.data=data.split("\n")
            self.data[1]=updated_name
            for data in self.data:
                f.write(str(data)+"\n")
            print("Your Name Has Been Updated.")
  def get_account_info(self):
    with open("bank_data.txt","r")as f:
      data=f.read()
      self.data=data.split("\n")
      print(f"Customers Details Are:\n Customer Name:{self.data[1]}\n Customer Phone Number:{self.data[3]}\n Account Balance:{self.data[0]}")
  def transfer_cash(self): 
    with open("bank_data.txt","r")as f:
      data=f.read()
      self.data=data.split("\n")   
    a=self.data[0]
    c=int(a)
    account_number=int(input("Enter Account Number To Whom You Want To Transfer Money: "))
    cash1=int(input("Enter Money You Want To Transfer: "))
    if cash1>c:
      print("Insufficient Balance")
    else:
      b=c-cash1
      print(f"Amount of RS {cash1} Sucessfully Trasfered To Account Number {account_number}")  
      print(f"Currently Your Account Balance is RS {b}")
      with open("bank_data.txt","r+")as f:
        self.data=data.split("\n")
        self.data[0]=b
        for data in self.data:
          f.write(str(data)+"\n")     
print('''1)REGISTER
2)LOGIN
3)ADD CASH
4)UPDATE PROFILE
5)GET ACCOUNT INFO
6)TRANSFER CASH''')
c1=Bank()
choice=int(input("Enter Your Choice:"))
if choice==1:
  c1.register_system()
if choice==2:
  c1.login_system()
if choice==3:
  c1.add_cash()
if choice==4:
  c1.update_profile()
if choice==5:
  c1.get_account_info()
if choice==6:
  c1.transfer_cash()
