data = [
    'kajak',
    'kot'
]


def is_palindrom(word):
    """
    Funkcja sprawdza czy podany argument jest palindromem
    :param word:
    :return:
    """
    word_reverse = word[::-1]
    if word == word_reverse:
        return True
    else:
        return False

# komentarz
# kod pominiety
"""
pomijamy
pomijamy
"""
while True:
    user_word = input('Input a word: ')
    for user_word in data:
        result = is_palindrom(word=user_word)
        print(f'{user_word}: {result}', end='')
        print('{1}: {0}'.format(user_word, str(result)))
    choice = input('End? y/n: ')
    if choice.lower() == 'y':
        break
pass