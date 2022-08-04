import random

def guessNumber(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Enter a number between 1 and {x}: '))
        if guess < random_number:
            print('Your guess is a bit low')
        elif guess > random_number:
            print('Your Guess is a bit high')
        
    print(f'Yes!! you guessed the number {random_number} correctly3')

# guessNumber(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':     
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'Is {guess} to high (H), to low (L), or correct(C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The Computer guessed your number {guess} correctly!')

computer_guess(10)