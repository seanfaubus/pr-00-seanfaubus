# from fileio import read_keyvalue, read_message
# # res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
def make_dictionary(l1, l2):
    # Write your code here
    dictionary = {l1[i]: l2[i] for i in range(len(l1))}
    return dictionary


def cipher(message, d):
    # Write your code here
    messagesToWrite = []
    cipheredMessage = ""
    for char in message:
        if char in d.keys():
            cipheredMessage += d[char]
        else:
            cipheredMessage += char
    messagesToWrite.append(cipheredMessage)
    # print('HI', messagesToWrite)
    return cipheredMessage

# l1 = read_keyvalue('ciphercode.txt')[0]
# l2 = read_keyvalue('ciphercode.txt')[1]
# print(l1)
# print(l2)
# booboo = make_dictionary(l1,l2)
# print(booboo)
# strang = 'please cipher this message'
# codeStrang = ''
# for i in strang:
#     if i in booboo.keys():
#         codeStrang += booboo[i]
#     else:
#         codeStrang += i
# print(codeStrang)
#
# print(cipher('please cipher this message', make_dictionary(l1,l1)))
# for message in read_message('messages.txt'):
#     print(cipher(message, make_dictionary(l1,l2)))