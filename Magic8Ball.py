#Magic8Ball.py
#Name: Jessica Pusher
#Date: 2.1.25
#Assignment: Magic8Ball.py

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball Assignment")
  #Prompt the user for their question.
  Question = input("Ask me anything...")
  answers = ["Heck no!","For sure!","Try a little harder!","Keep it positive",
             "You've got this!","Absolutely"]
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * length

  r = int(r)
  response = answers[r]

  print(response)



if __name__ == '__main__':
  main()
