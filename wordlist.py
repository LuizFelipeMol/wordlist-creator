import itertools

wordlist = []
variation_list = []

password_variations = {
    'a': ['a', 'A', '@', '4', '^'],
    'b': ['b', 'B', '8', '|3'],
    'c': ['c', 'C', '(', '<'],
    'd': ['d', 'D'],
    'e': ['e', 'E', '3', '&'],
    'f': ['f', 'F', 'ph'],
    'g': ['g', 'G', '9', '&'],
    'h': ['h', 'H', '#'],
    'i': ['i', 'I', '1', '!', '|'],
    'j': ['j', 'J'],
    'k': ['k', 'K', '|<'],
    'l': ['l', 'L', '1', '|'],
    'm': ['m', 'M'],
    'n': ['n', 'N', '^'],
    'o': ['o', 'O', '0', '*'],
    'p': ['p', 'P'],
    'q': ['q', 'Q'],
    'r': ['r', 'R', '2'],
    's': ['s', 'S', '$', '5'],
    't': ['t', 'T', '7', '+'],
    'u': ['u', 'U', 'v'],
    'v': ['v', 'V', 'u'],
    'w': ['w', 'W'],
    'x': ['x', 'X', '%'],
    'y': ['y', 'Y', '¥'],
    'z': ['z', 'Z', '2'],
}


def enter_word():

    while True:

        input_word = input('Enter a word or next step ')
        if input_word == 'next step':
            break
        else:
            wordlist.append(input_word.lower())

def create_password():
    for word in wordlist:
        print(word)

        variations = [password_variations[letter] if letter in password_variations else [letter] for letter in word]

        for combination in itertools.product(*variations):
            new_word = ''.join(combination)
            variation_list.append(new_word)

def output_wordlist():
    file_name = input('name for wordlist file ')
    file = open(f"{file_name}.txt", "a")
    for item in variation_list:
        file.write(item+', ')
    file.close()




        # for letter in word:
        #     print(letter)
        #
        #     if letter in password_variations:
        #         for variation in password_variations[letter]:
        #             new_word = word.replace(letter, variation)
        #             variation_list.append(new_word)
        #             print(wordlist, variation_list)



if __name__ == '__main__':
    enter_word()
    create_password()
    output_wordlist()
    print(wordlist, len(variation_list))


