#python quiz game
from time import sleep
def quiz_game():
  print("WELCOME TO ASK INDIA QUIZ")
  print("                        ")
  answer=input("Are You Ready To Play Quiz(yes/no)=")
  score=0
  incorrect=0
  skip=0
  total_questions=3
  if answer.lower()=='yes':
    print(" ")
    print("QUESTION 1: WHAT IS THE CAPITAL OF INDIA")
    print("1)Delhi")
    print("2)Mumbai")
    print("3)Skip Question")
    answer=input("Enter Your Choice=")
    print("Processing Result")
    sleep(1)
    if answer.lower()=='1':
      score+=1
      incorrect+=0
      skip+=0
      print(" ")
      print("correct answer")
      print(" ")
    elif answer.lower()=='3':
      score+=0
      print(" ")
      skip+=1
      print("You Have Skipped The Question Now Presenting Next Question\n")  
    else:
      print(" ")
      print("Wrong Answer")
      incorrect+=1
      skip+=0
      print(" ")
    print("QUESTION 2:Where Is Gateway Of India Situated")
    print("1)Goa")
    print("2)Mumbai")
    print("3)Skip Question")
    answer=input("Enter Your Choice=")
    print("processing result")
    sleep(1)
    if answer.lower()=='2':
      score+=1
      incorrect+=0
      skip+=0
      print(" ")
      print("correct answer")
      print(" ")
    elif answer.lower()=='3':
      score+=0
      print(" ")
      skip+=1
      print("You Have Skipped The Question Now Presenting Next Question\n")  
    else:
      print("")
      print("wrong answer")
      incorrect+=1
      skip+=0
      print(" ")      
    print("QUESTION 3:Wich One Is The Most Famous Search Engine")
    print("1)Google")
    print("2)Bing")
    print("3)Skip Question")
    answer=input("Enter Your Choice=")
    print("processing result")
    sleep(1)
    if answer.lower()=='1':
      score+=1
      incorrect+=0
      skip+=0
      print(" ")
      print("correct answer")
      print(" ")
    elif answer.lower()=='3':
      score+=0
      print(" ")
      skip+=1
      print("You Have Skipped The Question\n")  
    else:
      print(" ")
      print("wrong answer")
      incorrect+=1
      skip+=0
      print(" ")  
    print("THANKS FOR PLAYING THIS QUIZ") 
    print("  ")
    print("YOUR RESULT IS:") 
    print(" ")
    print("Number Of Questions Answered Correct=",score)
    print("Number Of Questions Answered Incorrect=",incorrect) 
    print("Number Of Questions Skipped=",skip) 
    mark=(score/total_questions)*100
    print("Marks Obtained Are",mark)
  else:
    print("BYE")  
quiz_game()   
