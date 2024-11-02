import random as rnd

def generate():
    ls_letter = 'qwertyuiopasdfghjklzxcvbnm'
    ls_number = '0123456789'
    ls = ls_letter + ls_number
    block = ['' for i in range(5)]
    for i in range(5):
        block[i] = rnd.choice(ls)
    return ''.join(block).upper()

def shake(word, number, ind):
    ls_letter = ('abcdefghijklmnopqrstuvwxyz').upper()
    ls_number = '0123456789'
    ls = list((ls_letter + ls_number))
    letters = list(word)
    new_word = []
    if ind%2 == 0:
        for i in range(len(letters)):
            step = ls.index(letters[i]) + number
            if step > len(ls) - 1:
                step = step - len(ls)
            new_word.append(ls[step])

    elif ind%2 != 0:
        for i in range(len(letters)):
            step = ls.index(letters[i]) - number
            if step < 0:
                step = len(ls) + step
            new_word.append(ls[step])
    return(''.join(new_word)[1:])