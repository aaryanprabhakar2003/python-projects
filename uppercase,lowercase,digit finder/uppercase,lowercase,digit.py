with open("data.txt")as f:
 c=f.read()
uppercase=0
lowercase=0 
digit=0
for i in c:
  if i.isupper():
    uppercase+=1
  elif i.islower():
    lowercase+=1
  elif i.isdigit():
    digit+=1  
  else:
    pass
f=open("data.txt","a")
f.write("TOTAL NO OF UPPERCASE LETTERS ARE= ")
f.write(str(uppercase))
f.write("\nTOTAL NO OF LOWERCASE LETTERS ARE= ")
f.write(str(lowercase))
f.write("\nTOTAL NO OF DIGITS ARE= ")
f.write(str(digit))