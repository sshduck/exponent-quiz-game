import random
import time


def number_format(num):
    if num >= 1024 ** 4:
        return f"{num // (1024 ** 4)}T"
    elif num >= 1024 ** 3:
        return f"{num // (1024 ** 3)}B"
    elif num >= 1024 ** 2:
        return f"{num // (1024 ** 2)}M"
    elif num >= 1024:
       return f"{num // 1024}K"
    else:
        return str(num)

def exponent_quiz():
    #get the powers of 2 from 0 through 49 somehow
    #randomize them
    #give them to the user, ask for input
    #check input against correct
    #if correct move on if incorrect make them try again
    #do not repeat the questions
    #end when all 50 are complete

    print("How well do you know the powers of two? \nBe sure to round using T,B,M, and K. ")
    starttime = time.time()

    exponentlist = []
    for num in range(0,49):
        exponentlist.append(num)

    random.shuffle(exponentlist)

    for value in exponentlist:
        correct = 2 ** value
        rounded = number_format(correct)

        while True:
            answer = input(f"What is the base ten value of 2 ** {value}? ").strip()
            if answer == rounded:
                print("Correct! Continue.")
                break
            elif answer == "help bruh idek":
                print(f"{rounded}")
            else:
                print("Wrong! Try again.")
    

    endtime = time.time()

    timespent = endtime - starttime
    print(f"You finished in: {timespent:.3f} seconds total. \nTry again!")


if __name__ == "__main__":
    exponent_quiz()