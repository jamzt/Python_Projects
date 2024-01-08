#
# Python: 3.11.4
# 
# Author: Jamie Taalai
# 
# Purpose: Python course, creating our first program together with Tech Academy.
#          Demonstrating how to psdd variables from functiion
#          While producing functional game.
# 
#          Remember, function_name(variable) __means that we pass in the varaible. 
#          return varaible means_that we are returning the varaible back to the calling function.




def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_name(f_name, l_name, age, gender)


def get_name(f_name, l_name, age, gender):
    print("My name is {} {}. I am {} year old {}.".format(f_name,l_name,age,gender))



if __name__ == "__main__":
    start()
    
