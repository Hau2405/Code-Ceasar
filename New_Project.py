q = str(input("Enter a word: "))
n = int(input("Nhap buoc nhay: "))
#encode
def encode(q,n):
    char_list = list(q)

    for i in range(len(char_list)):
        letter = char_list[i]
        if letter.islower():
            char_list[i] = chr(((ord(letter) - ord('a') + n ) % 26) + ord('a'))
        elif letter.isupper():
            char_list[i] = chr(((ord(letter) - ord('A') + n ) % 26) + ord('A'))
        else:
            char_list[i] = chr(ord(letter) + n )

    shift = ''.join(char_list)
    return shift
encode_save = encode(q,n)
#decode
def decode(q,n):
    char_list = list(q)

    for i in range(len(char_list)):
        letter = char_list[i]
        if letter.islower():
            char_list[i] = chr(ord('z')-((ord('z')-ord(letter) + n ) % 26))
        elif letter.isupper():
            char_list[i] = chr(ord('Z')-((ord('Z')-ord(letter) + n ) % 26)) 
        else:
            char_list[i] = chr(ord(letter) - n)

    shift = ''.join(char_list)
    return shift

print(encode(q,n))
print(decode(encode_save,n))