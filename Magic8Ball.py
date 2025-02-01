#Magic8Ball.py
#Name: Jessica Pusher
#Date: 2.1.25
#Assignment: Magic8Ball.py

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("What should I make for dinner tonight?")
  #Prompt the user for their question.
  answers = ["Italian Food","Mexican Food","Thai Food","American Food","Go Out to Eat"]
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * length

  r = int(r)
  response = answers[r]

  print(response)



if __name__ == '__main__':
  main()
