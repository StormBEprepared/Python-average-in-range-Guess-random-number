import random

low=1
high=101#In a random range the higher value in range is excluded from the range of numbers that can be displayed

class NumberGuessing:
    def Nguess():
        randomNumber= random.randint(low,high)
        print(f"Guess the random number between {low} and {high} exclusivelly")    
        attempts=0
        while True:
            userNumber= input("Enter your guess:")
            userNumber = int(userNumber)
            
            if userNumber==randomNumber:
                attempts+=1
                print(f"Congrats! You guessed it from {attempts} attempt{'s' if attempts>1 else ''}!") 
                break
            elif randomNumber-10<=userNumber<=randomNumber+10:
                attempts+=1
                print(f"You are close!")
            else:
                attempts+=1
                print("Keep trying!")
        
       
NumberGuessing.Nguess()