def read_keyvalue(filename):
    # Write your code here
    # Getting file input
    path = "input/"
    with open(path+filename, 'r') as f:
        keyLetters = []
        valueLetters = []
        text = f.readlines()
        for i in text:
            if i.startswith('K'):
                keyLetters.append(i[3:])
                keyLetters = [char for word in keyLetters for char in word]
                # keyLetters.pop()
                # keyLetters.append(' ')
                for i in range(len(keyLetters)):
                    if keyLetters[i] == '\n':
                        keyLetters[i] = ' '
            else:
                valueLetters.append(i[3:])
                valueLetters = [char for word in valueLetters for char in word]
        return keyLetters, valueLetters


def read_message(filename):
    # Write your code here
    # Getting file input
    path = "input/"
    with open(path+filename, 'r') as f:
        text = f.readlines()
    pass

def write_ciphered_messages(ciphered_message, filename):
    # Write your code here
    pass


print(read_keyvalue('ciphercode.txt'))