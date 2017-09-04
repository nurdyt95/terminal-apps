## Project_01_Terminal_Apps
## Date: 31/08/2017    
## nurdy

import random, time

def welcome():
    prepeat = 'n'
    while prepeat.lower() != 'y':
        pname = str(input('Enter your player name: '))
        print('Welcome.', pname)
        time.sleep(1)
        print('Is %s the correct player ? y or n ' % pname)
        prepeat = str(input())

    question()

def question():
    global value
    global score
    global timeclock
    score = 0
    questionNum = range(1,6)
    print('This is an arithmetic test, you will be scored /%s.' % len(questionNum))
    time.sleep(2)
    for x in questionNum:
        ## generate random even numbers
        num_1 = random.randint(1,6) * 2
        num_2 = random.randint(1,6) * 2
        operators = {'Multiplcation':'*','Division':'/', 'Addition':'+', 'Subtraction':'-'}
        operation = random.choice(list(operators.values()))
        print('What is ', num_1, operation, num_2,'?')

        # def checkType(value):
        #     isInteger = int(value)
        #     if value == isInteger:
        #         return value
        #     else:
        #         operation1()
    
        
        if operation == '*':
            value = (num_1 * num_2)
            
        elif operation == '/':
            value = (num_1 / num_2)

        elif operation == '+':
            value = (num_1 + num_2)
            
        elif operation == '-':
            value = (num_1 - num_2)

    ##    count = list(reversed(range(1,6)))
    ##    
    ##    for x in count:
    ##        print(x)
    ##        time.sleep(1)

        timeclock = round(time.clock(),3)
            
        answer()

    time.sleep(1)
    
    if score > len(questionNum)/2:
        print('Congratulations!, you scored %s / %s' % (score, len(questionNum)))
    else:
        print('Better luck next time, you scored %s / %s' % (score, len(questionNum)))
        
    time.sleep(1)
    print('--- %s seconds ---' %(timeclock))
    time.sleep(1)
    
    
    playAgain()

    
def answer():
    global score
    try:
        choice = int(input())
        if choice == value:
            print('Correct')
            score = score + 1
        else:
            print('Incorrect')
    except:
            print('Please enter integers only')


def playAgain():
    print('Would you like to play again? y or n')
    pagain = str(input())
    if pagain.lower == 'n' or 'no':
        print('Thanks for playing')
        print("""
                                                                          
                     _           _    _                            _      
 ___  ___  ___  ___ | |_  ___  _| |  | |_  _ _    ___  _ _  ___  _| | _ _ 
|  _||  _|| -_|| .'||  _|| -_|| . |  | . || | |  |   || | ||  _|| . || | |
|___||_|  |___||__,||_|  |___||___|  |___||_  |  |_|_||___||_|  |___||_  |
                                          |___|                      |___|

        """)
        time.sleep(3)
        exit
    elif pagain.lower == 'y' or 'yes':
        welcome()
    else:
        welcome()

if __name__ == "__main__":
   welcome()
