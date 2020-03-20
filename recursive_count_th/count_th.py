'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    counter = 0 # Set empty var
    if len(word) <= 1: # if the word lenght is shorter then th
        return counter # return 0
    elif word[0] + word[1] == 'th': # if word contains th
        counter = count_th(word[1:]) + 1 # add one to the count and
        # run with the first 2 characters not in the word
    else:
        counter = count_th(word[1:]) # if woord has no th contiue
    return counter

print(count_th("etheral"))