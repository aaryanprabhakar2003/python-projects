#print('''1)ENTER MARKS
#2)EXIT ''')
'''user=int(input("Enter your choice:"))
if user==1:
    store_data={}
    choice=int(input("For How Many Subjects You Want To Enter Marks:"))
    for i in range(choice):
        subject=input("Enter Subject Name:")
        marks=float(input("Enter Marks:"))
        store_data[subject]=marks
    print(store_data)
    values=store_data.values()
    total=sum(values)
    print(total)
    total1=total/choice
    print(f"Your Average Marks in {choice} Subjects are {total1}")
    if total1>=91 and total1<=100:
        print("Your Grade Is A1")
    elif total1>=81 and total1<=91:
        print("Your Grade Is A2")
    elif total1>=71 and total1<=81:
        print("Your Grade Is B1")
    elif total1>=61 and total1<=71:
        print("Your Grade Is B2")
    elif total1>=51 and total1<=61:
        print("Your Grade Is C1")
    elif total1>=41 and total1<=51:
        print("Your Grade Is C2")   
    elif total1>=31 and total1<=41:
        print("Your Grade Is D") 
    elif total1>=21 and total1<=31:
        print("Your Grade Is E1")
    elif total1>=0 and total1<=21:
        print("Your Grade Is E2") '''



#print('''1)ENTER MARKS
#2)EXIT ''')
'''user=int(input("Enter your choice:"))
if user==1:
    store_data={}
    choice=int(input("For How Many Subjects You Want To Enter Marks:"))
    for i in range(choice):
        subject=input("Enter Subject Name:")
        grade=input("Enter Grade:")
        credits=float(input("Enter Credits:"))
        store_data[subject]=credits
    #print(store_data)
        values=store_data.values()
        total=sum(values)
        if grade=="A" or grade=="a":
            result1=credits*4
            print(result1)    
        elif grade=="B" or grade=="b":
            result2=None
            result2=credits*3
            print(result2)
        elif grade=="C" or grade=="c":
             result3=credits*2
             print(result3)
        elif grade=="D" or grade=="d":
            result4=credits*1
            print(result4)
        elif grade=="E" or grade=="e":
            result5=credits*0.5
            print(result5)
        elif grade=="F" or grade=="f":
            result6=credits*0
            print(result6)
    #print(total)     #credits total
    result=result1+result2+result3+result4+result5+result6 
    print(result)    '''                           #grade total

d={}
while True:
    flag=True
    sub= input("Enter Subject Name: \n Press y To Exit: ")
    if sub=='y':
        break
    d[sub]=[]
print(d)


def gpcal(grade):
    if grade=='a' or grade=="A":
        res=4.5
    elif grade=='b' or grade=="B":
        res=4.0
    elif grade=='c' or grade=="C":
        res=3.5
    return res

for i in d:
    while True:
        lettergrade=input(f"Enter Letter Grade For {i}: ")
        creditpoint=float(input(f"Enter Credit Point For {i}"))
        gradepoint = gpcal(lettergrade)
        #print(f"Your letter grade for {i}: {lettergrade}")
        #print(f"Your creditpoint for {i}: {creditpoint}")
        #print(f"Your grade point for {i}: {gradepoint}")
        ask=input("Press 1 To Confirm Or 2 To Enter Again")
        if ask=='1':
            d[i]=[lettergrade,creditpoint,gradepoint]
            break
        else:
            continue
 # print(d)
totalgp=0
totalcreditunit=0
for i in d.values():
    totalgp+=i[2]
    totalcreditunit+=i[1]

gpa=totalgp/totalcreditunit
#print(gpa)
for i in d:
    print(f" Course Info Student Grade As Follows :{i}")
    print(f"The GPA For This Student With  Courses Will Be ")
for i in d.values():
    print(f"({i[1]}*{i[2]})+")
print("-------------------------")
for i in d.values():
    total_sum=(i[1]*i[2])
    total_credit_sum=(i[2])
    tota_sum_credit_str=int(total_credit_sum)
    print(sum(tota_sum_credit_str))
    print(f"Total of Above {totalgp} / Sum Of All Credits {totalcreditunit}")
    
