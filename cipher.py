from fileio import read_keyvalue
# res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
def make_dictionary(l1, l2):
    # Write your code here
    dict = {l1[i]: l2[i] for i in range(len(l1))}

    return dict

def cipher(message, d):
    # Write your code here
    pass

l1 = read_keyvalue('ciphercode.txt')[0]
l2 = read_keyvalue('ciphercode.txt')[1]
print(make_dictionary(l1,l2))