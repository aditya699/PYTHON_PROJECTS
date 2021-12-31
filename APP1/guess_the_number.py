import random 
print ("Welcome to aditya's game here the computer will generate  a number if u guess \
correctly in 2 iterations your money will be doubled note numbers are from 1 to 10 only ")
def game():
    random_number=random.randint(1,10)
    amount=int(input("How many ruppes you to invest: "))
    user_input=int(input("Please enter the number that think the computer has genrated: "))
    count=0
    if random_number==user_input:
        print("Wow you have guessed the number correctly in the first iteration of the game")
    else:
        count=1
        while random_number!=user_input:
            count+=1
            if random_number>user_input:
                print("The number you are trying to guess is too low")
            else:
                print("The number you are trying to guess is too high")
            user_input=int(input("Please enter the number that think the computer has genrated: "))


    if(count <=2):
        print("Your money has been doubled")
        x=amount*2
        print(f"Here you win {x} ruppes")
    else:
        print("Sorry u may have gussed the number but u took more than two interations")

game()