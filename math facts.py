# This script will test your math facts
import random
import time

wrong = 0

def instructions():
    print('This program will test your math facts.')
    time.sleep(3)
    print('You will be asked a series of 20 questions.')
    time.sleep(3)
    print('Your goal is to answer each question as fast as possible.')
    time.sleep(3)
    print('To answer, type a number and then hit enter.')
    time.sleep(3)
    print('If you answer incorrectly, the game will end.')
    time.sleep(5)
    
def ready_set_go():
    print('Ready!')
    time.sleep(1)
    print('Set')
    time.sleep(1)
    print('Go')
    time.sleep(1)

def math_game():
    global wrong
    list_of_numbers = [0,1,2,3,4,5,6,7,8,9]
    list_of_signs = ['+','-','*','/']
    number = random.choice(list_of_numbers)
    #print(number)
    number1 = random.choice(list_of_numbers)
    #print(number1)
    sign = random.choice(list_of_signs)
    #print(sign)
    if sign == '+':
        correct_answer = number+number1
        print(number,'+',number1)
        user_answer = int(input())
        correct_answer = number+number1
        #print(correct_answer)
        #print('Your answer:',user_answer)
        if user_answer == correct_answer:
            print('correct')
        else:
            print('wrong')
            wrong = wrong + 5
    if sign == '-':
        correct_answer = number+number1
        print(number,'-',number1)
        user_answer = int(input())
        correct_answer = number-number1
        #print(correct_answer)
        #print('Your answer:',user_answer)
        if user_answer == correct_answer:
            print('correct')
        else:
            print('wrong')
            wrong = wrong + 5
    if sign == '*':
        correct_answer = number+number1
        print(number,'*',number1)
        user_answer = int(input())
        correct_answer = number*number1
        #print(correct_answer)
        #print('Your answer:',user_answer)
        if user_answer == correct_answer:
            print('correct')
        else:
            print('wrong')
            wrong = wrong + 5
    if ((sign == '/') and (number1 == 0)):
        new_sign = '+'
        print(number,new_sign,number1)
        new_correct_answer = number+number1
        user_answer = int(input())
        if user_answer == new_correct_answer:
            print('correct')
        else:
            print('wrong')
            wrong = wrong + 5
    elif ((sign == '/') and (number/number1 != int(number/number1))):
        new_sign = '+'
        print(number,new_sign,number1)
        new_correct_answer = number+number1
        user_answer = int(input())
        if user_answer == new_correct_answer:
            print('correct')
        else:
            print('wrong')
            wrong = wrong + 5
    elif ((sign == '/') and (number/number1 == int(number/number1))):
        correct_answer = number+number1
        print(number,'/',number1)
        user_answer = int(input())
        correct_answer = number/number1
        #print(correct_answer)
        #print('Your answer:',user_answer)
        if user_answer == correct_answer:
            print('correct')
        else:
            print('wrong')
            wrong = wrong + 5
            
def question_counter():
    global wrong
    count = 0
    while (count <= 19) and (wrong == 0):
        count = count + 1
        print('Question:',count)
        math_game()
        print('------------------------------------------------------')
        
        
            
#instructions()
#ready_set_go()
#math_game()
start = time.time()
question_counter()
end = time.time()
print('Your time:',end-start)