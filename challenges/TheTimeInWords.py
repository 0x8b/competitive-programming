h = int(input())
m = int(input())

def word(n):
    return ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fiveteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'][n]

def time_in_words(h, m):
    if m == 0:
        print(word(h), 'o\' clock')
    elif m == 15:
        print('quarter past', word(h))
    elif m < 30:
        minutes = ''

        if m == 1:
            minutes = 'one minute past'
        elif m > 20:
            minutes = 'twenty ' + word(m - 20) + ' minutes past'
        else: # 2 - 20
            minutes = word(m) + ' minutes past'

        print(minutes, word(h))
    elif m == 30:
        print('half past', word(h))
    elif m == 45:
        print('quarter to', word(h + 1))
    else: # 31 to 59 except 45
        minutes = ''
        to = 60 - m

        if to > 20:
            minutes = 'twenty ' + word(to - 20) + ' minutes to'
        else:
            minutes = word(to) + ' minutes to'

        if m == 1:
            minutes = 'one minute to'
        print(minutes, word(h + 1))

time_in_words(h, m)