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
