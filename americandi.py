# neighbor --- neightbour
# has to be between or


vowels = ['a','e','i','o','u']


while True:
    words = input()
    if len(words) > 4 and 'or' in words:
        word = words.split('or')
        if word[0][-1] not in vowels and len(str(word[1])) == 0:
            print(''.join(word[0]+'our'))
        else:
            print(''.join(words))
    elif words == 'quit!':
        break
    else:
        print(words)

    



