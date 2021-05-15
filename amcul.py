#start

import os
import time
from colorama import init, Fore #Color
init()

#Def foe clear
def Clear():  
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
time.sleep(3)

#Logo of tool
logo =print(Fore.RED+"""
_nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Hi! i am Amir|
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--""")
time.sleep(1)

#About the programmer
print(Fore.YELLOW+"""###########################
|  WRITE BY AMIR....       |  
|  ID RUBIKA : @am_1384s   |
|  ID TEl : @am_1384s      |
###########################""")
time.sleep(3)

#Welcome to Cuculate
welcome=print(Fore.GREEN+"""
{----Hi baby :) I am Amir and I want to cuculate your math----}\n
##########################################################""")
time.sleep(3)

#About the tool
print(Fore.BLUE+"""
__________________________________
|You can use of my cuculator to  |
|cuculate your math. For example |
|you can do power two number with|
|together or do other cuculates  |
|with this.....................  |
==================================\n
##########################################################""")
time.sleep(2)

#Enter two number to cuculate
number_1 = int(input(Fore.BLUE+"=>"+Fore.LIGHTWHITE_EX+"Enter your first number baby ;) : "))
time.sleep(2)
number_2 = int(input(Fore.BLUE+"=>"+Fore.CYAN+"Enter your second number baby ;) : "))
time.sleep(2)
print(Fore.LIGHTCYAN_EX+"##########################################################\n")

#script of define about mark
operation =print(Fore.LIGHTRED_EX+
"""Please Baby type in the math operation you would like to complete:""")
time.sleep(0.8)
print(Fore.BLUE+
"""+ for addition""")
time.sleep(0.8)
print(Fore.YELLOW+
"""- for subtraction""")
time.sleep(0.8)
print(Fore.GREEN+
"""* for multiplication""")
time.sleep(0.8)
print(Fore.LIGHTCYAN_EX+
"""÷ for division""")
time.sleep(0.8)
print(Fore.RED+
"""** for power""")
time.sleep(0.8)

#Script of Enter a murk
operation=input(Fore.BLUE+"=>"+Fore.CYAN+"Enter a mark: ")
print("\n")

#Give some information to cuculate a math
time.sleep(4)
print(Fore.YELLOW+"##########################################################\n")
if operation == '+':
    output_number = number_1 + number_2
    print( "{} + {} = {}" .format(number_1, number_2, output_number))
elif operation == '-':
    output_number = number_1 - number_2
    print( "{} - {} = {}" .format(number_1, number_2, output_number))
elif operation == '*':
    output_number = number_1 * number_2
    print( "{} * {} = {}" .format(number_1, number_2, output_number))
elif operation == '÷':
    output_number = number_1 / number_2
    print( "{} / {} = {}" .format(number_1, number_2, output_number))
elif operation == '**':
    output_number = number_1 ** number_2
    print( "{} ** {} = {} " .format(number_1, number_2, output_number))

#if User otherthing istead of the Numbers
else:
        print(Fore.MAGENTA+"Amir could not do your calculation")
calc_again = input(Fore.LIGHTBLUE_EX+"""
Now You must Write(N) to finish this cuculate! please write (N): """)

#the massage of about Bye
if calc_again.upper() == 'N':
    time.sleep(0.8)
    print(Fore.MAGENTA+"Good Bye Baby :)")
    time.sleep(0.5)
    print(Fore.GREEN+"See you soon Baby ;)")
