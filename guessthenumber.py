import time
import random
def guess(a):
   b= random.randint(-1000000000000000,1000000000000000)
   if a == b:
       time.sleep(2)
       print('Congratulations! You guessed the number correctly.')
   elif a not in range(-1000000000000000,1000000000000000):
       time.sleep(1)
       print('Pls Stay within the limit')
   elif a < b:
       time.sleep(2)
       print('Your guess is too low. Try a higher number.')
   elif a > b:
       time.sleep(2)
       print('Your guess is too high. Try a lower number.')
   
   
print("Wellcome to the guessing game of mine\nHere the task is you have to guess a number an integer to be exact (in between -1000000000000000 to 1000000000000000)\nYour system will also guess a random integer ( in between -1000000000000000 to 1000000000000000)\nIf your guess matched with your system you win")
a=int(input("Enter a random integer "))
guess(a)