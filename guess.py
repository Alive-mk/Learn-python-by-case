import random
guessToken = 0

myname = input()
print("hello "+myname+" hello")#concatenation of string
number = random.randint(1, 20)
for guessToken in range(6):
    guess = input()
    guess = int(guess)
    # if guess > number:
    #     print("bigger")
    # if guess < number:#this is a problem, we should use elif instead.
    #     print("smaller")
    # else:
    #     print("right")
    #     break
    if guess > number:
        print("bigger")
    elif guess < number:
        print("smaller")
    else:
        print("right")
        break
if guess != number:
    print("wrong")
