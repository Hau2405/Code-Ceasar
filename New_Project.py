q = str(input("Enter a word: "))
n = int(input("Nhap buoc nhay: "))
#encode
def encode(q,n):
    char_list = list(q)

    for i in range(len(char_list)):
        letter = char_list[i]
        if letter == 'z':
            char_list[i] = chr(((ord(letter) - ord('a') + n ) % 26) + ord('a'))
        elif letter == 'Z':
            char_list[i] = chr(((ord(letter) - ord('A') + n ) % 26) + ord('A'))
        elif letter == '':
            char_list[i] = chr(ord(''))
        else:
            char_list[i] = chr(ord(letter) + n )

    shift = ''.join(char_list)
    return shift

#decode
def decode(q,n):
    char_list = list(q)

    for i in range(len(char_list)):
        letter = char_list[i]
        if letter == 'a':
            char_list[i] = chr(ord('z')-((ord('z')-ord(letter) + n ) % 26))
        elif letter == 'A':
            char_list[i] = chr(ord('Z')-((ord('Z')-ord(letter) + n ) % 26)) 
        else:
            char_list[i] = chr(ord(letter) - n)

    shift = ''.join(char_list)
    return shift
print(encode(q,n))