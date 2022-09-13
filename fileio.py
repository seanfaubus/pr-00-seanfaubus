def read_keyvalue(filename):
    # Write your code here
    # Getting file input
    # path = "input/"
    with open(filename, 'r') as f:
        keyLetters = []
        valueLetters = []
        text = f.readlines()
        for i in text:
            if i.startswith('K'):
                keyLetters.append(i[3:])
                keyLetters = [char for word in keyLetters for char in word if char != ' ']
                keyLetters2 = keyLetters[:]
                for i in range(len(keyLetters2)):
                    if keyLetters2[i] == '\n':
                        keyLetters2.remove(keyLetters2[i])

            else:
                valueLetters.append(i[3:])
                valueLetters = [char for word in valueLetters for char in word  if char != ' ']
        return keyLetters2, valueLetters


def read_message(filename):
    # Write your code here
    # Getting file input
    # path = "input/"
    messages = []
    with open(filename, 'r') as f:
        text = f.readlines()
        for line in text:
            messages.append(line.strip())
        # run message through cipher?
    # print(messages)
    return messages

### FIXME trying to see total output

def write_ciphered_messages(ciphered_message, filename):
    # Write your code here
    # path = 'output/'
    with open(filename, 'a') as f:
        f.write(ciphered_message + '\n')
        


# l1 = read_keyvalue('ciphercode.txt')[0]
# l2 = read_keyvalue('ciphercode.txt')[1]
# print(l1)
# print(l2)
# print(len(l1))
# print(len(l2))

# print(read_message('messages.txt'))