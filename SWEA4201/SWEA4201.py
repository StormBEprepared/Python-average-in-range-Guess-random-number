import sys
import statistics


inputString= input('Please enter the numbers separated by a space:')
print("\n")
userList = inputString.split();
print('The numbers that you have entered are: ', userList)

for i in range(len(userList)):    # convert each item to int type
    userList[i] = int(userList[i])

def average(y):
    return sum(y)/len(y)


def optionChoosing(x):
    inputOption = input('Press: 1) Exit.  2) Calculate the average of the numbers that you gave.')
    inputOption= int(inputOption)
    if inputOption==1:
        sys.exit()
    elif inputOption==2:
        print('The average of the given number is:', average(x))
        print('The median number is:', statistics.median(x))
        Success=True
    else:
        print("Unrecognised input.")


Success=False
while Success==False:
    optionChoosing(userList)