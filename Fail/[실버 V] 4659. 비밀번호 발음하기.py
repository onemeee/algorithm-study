def program(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    pw_list = list(word)
    for wo in pw_list:
        if wo not in vowel:
            print(f'<{wo}> is not acceptable')

try:
    pw = input()
    program(pw)
except:
    pass