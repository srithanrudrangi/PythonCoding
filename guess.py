import random
guessesTaken = 0
print('Hello What is your name ?')
myname = input()
number = random.randint(1, 20)
print('Well, ' + myname +
      '. I am thinking of a number between 1 and 2.  Can you guess in 6 attempts ?')
while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    elif guess == number:
        print('Awesome!  Your guess is correct.')
        break
