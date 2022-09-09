from collections import Counter
def decrypt_ceasar(key, ciphertext):
    dec = ''
    for c in ciphertext:
        c_new = (c-key)%26
        dec += str(c_new)
    return dec

def encrypt_ceasar(key, plaintext):
    enc = []
    for c in plaintext:
        c_new = (c+key)%26
        enc.append(c_new)
    return enc

def hack_ceasar(ciphertext):
    for i in range(0, 27):
        dec = decrypt_ceasar(i, ciphertext)
        print('key: ', i)
        print(decode_num(dec))

# decrypts affine chiffre with key
def decrypt_affine(key, ciphertext):
    a_inverse = modular_inverse(key[0])
    b = key[1]
    print('Inverse of a:', a_inverse)
    decrypted = []
    for c in ciphertext:
        decrypted.append(((c-b)*a_inverse) % 26)
    return decrypted

# calculates greates common divisor of x and y
def gcd(y,x):
    while (y):
        x, y = y, x % y
    return abs(x)

# brute forces possible keys with educated guess based on frequencies
# prints and returns all possible keys
def hack_affine(match1, match2):
    # brute force approach
    x1, y1 = match1
    x2, y2 = match2
    inv = modular_inverse((x2-x1))
    a = (y2-y1)*inv % 26
    b = (y1-a*x1) % 26
    return (a,b)

    # for a in range(26):
    #     if gcd(a, 26) != 1:
    #         continue
    #     for b in range(26):
    #         if (a*x1 + b) % 26 == y1 and (a*x2 + b)%26 == y2:
    #             print('possible key: ('+str(a)+','+str(b)+')')
    #             keys.append((a,b))
    # return keys

# calculates modular inverse of interger a in group Z_n
def modular_inverse(a, n = 26):
    for i in range(n):
        if i*a % n == 1: return i

# counts occurrence of each letter
def letter_frequ(ciphertext):
    return Counter(ciphertext)

# encodes characters (a to z) to numbers (0 to 25)
# returns list of numbers
def encode_num(text):
    encoding = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
                'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    encoded = []
    for c in text.lower():
        encoded.append(encoding[c])
    return encoded

# decodes numbers (0 to 25) to characters (a to z)
# returns string
def decode_num(text):
    encoding = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
                'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    decoded = ""
    for n in text:
        decoded += list(encoding.keys())[n]
    return decoded


def dec_perm(key, cipher):
    decrypted = cipher
    for c in key:
        decrypted = decrypted.replace(key[c], c.upper())
    return decrypted

def enc_perm(key, plain):
    encrypted = plain
    for c in key:
        encrypted = encrypted.replace(c, key[c])
    return encrypted

def frequ_pair(text):
    frq = {}
    for i in range(len(text)-1):
            pair = text[i]+text[i+1]
            if pair in frq:
                frq[pair] += 1
            else:
                frq[pair] = 1
    return frq

def frequ_triple(text):
    frq = {}
    for i in range(len(text)-2):
        triple = text[i] + text[i+1] + text[i+2]
        if triple in frq:
            frq[triple] +=1
        else:
            frq[triple] = 1
    return frq

def double_letters(text):
    doubles = {}
    for i in range(len(text)-1):
        if text[i] != text[i+1]: continue
        pair = text[i]+text[i+1]
        if pair in doubles:
            doubles[pair] += 1
        else: doubles[pair] = 1
    return doubles