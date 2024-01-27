'''
    CS5001
    Homework 1, 9/13/2022
    Fall 2022
    Mohammad Toutiaee
'''


def main():
    # Your code goes here
    current_year = 2021
    user_name = input("Welcome! What is your name? ")
    print("Hi, " + user_name + ".")
    response = input("How old are you? ")
    user_age = int(response)
    user_birth = current_year - user_age
    print("You were born in " + str(user_birth) + ".")

main()
