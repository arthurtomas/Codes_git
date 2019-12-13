from random import randrange
pc_number = randrange(0, 101)
user_number = 200
count_attempt = 1
print('From 0 to 100, can you guess the number I thought? ')
while user_number != pc_number:
    user_number = int(input('{} attempt: '.format(count_attempt)))
    if user_number == pc_number:
        print('Congratulations! I really chose number {}!'.format(pc_number))
    else:
        print('{}? Absolutely not. Try again! '.format(user_number))
        count_attempt += 1
        if user_number < pc_number:
            print('Your choice was smaller than mine.')
        else:
            print('Your choice was bigger than mine.')
print('It took you {} attempt(s) to guess! '.format(count_attempt))
