#The Atbash cipher is an encryption method in which each letter of a word is replaced with 
#its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
def Atbash_cipher(text)->str:
    '''Function takes a string and applies the Atbash cipher to it'''
    alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
    ALPHA = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    alpha_copy = alpha.copy()
    ALPHA_copy = ALPHA.copy()
    alpha_copy.reverse()
    ALPHA_copy.reverse()
    result = ''
    for ch in text:
        if ch in alpha:
            val = alpha_copy[alpha.index(ch)]
            result+=val
        elif ch in ALPHA:
            val = ALPHA_copy[ALPHA.index(ch)]
            result+=val
        else :
            result+=ch
    return result

test_cases = ["apple","Hello world!","Christmas is the 25th of December"]
for case in test_cases:
    print(f'atbash("{case}")->"{Atbash_cipher(case)}"\n')
