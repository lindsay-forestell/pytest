import numpy as np


def random_list_chunk(my_list, n_return):
    """Creates a short and shuffled version of the input list.

    Args:
        my_list (list): Input list
        n_return (list): Length to return

    Returns:
        list: shuffled truncated list 
    """

    copied_list = my_list.copy()
    np.random.shuffle(copied_list)

    return copied_list[:n_return]


def guess_a_number(max_guesses=10):

    random_number = np.random.randint(100)

    guess_count = 0
    guess = int(input('Guess a number: '))

    while guess_count < max_guesses:

        if guess == random_number:
            print(f'Congratulations! The secret number was {random_number}.')
            return

        elif guess < random_number:
            string_start = 'Too low'
            guess_count += 1

        else:
            string_start = 'Too high'
            guess_count += 1

        if guess_count < max_guesses:
            guess = int(input(f'{string_start}. You have {max_guesses-guess_count} guesses remaining. Guess again: '))      
        else:
            print(f'Unlucky. The secret number was {random_number}.')
