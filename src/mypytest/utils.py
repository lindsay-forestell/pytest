import numpy as np
import pandas as pd
from .plotting import plot_hist


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
            guess_left = max_guesses-guess_count
            guess = int(input(f'{string_start}. You have {guess_left} guesses remaining. Guess again: '))
        else:
            print(f'Unlucky. The secret number was {random_number}.')


def plot_histogram(x):
    # make into an arbitrary pandas df to require the package be installed
    df = pd.DataFrame(columns=['x'], data=x)
    plot_hist(df, 'x')


def mad_libs():
    w1 = input('Provide a noun: ')
    w2 = input('Provide a plural noun: ')
    w3 = input('Provide a present tense verb: ')
    w4 = input('Provide a present tense verb: ')
    w5 = input('Provide a body part (plural): ')
    w6 = input('Provide an adjective: ')
    w7 = input('Provide a plural noun: ')
    w8 = input('Provide an adjective: ')

    if w6[0].lower() in 'aeiou':
        w6_prefill = 'an'
    else:
        w6_prefill = 'a'

    mad_lib_story = f"""
    Today, every student has a computer small enough to fit into his {w1}.
    He can solve any math problem by simply pushing the computer's little {w2}.
    Computers can add, multiply, divide and {w3}.
    They can also {w4} better than a human.
    Some computers are {w5}.
    Others have {w6_prefill} {w6} screen that shows all kinds of {w7} and {w8} figures.
    """

    print(mad_lib_story)
