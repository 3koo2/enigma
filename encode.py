import random

def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    # initialize ciphertext
    ciphertext = ''
    
    # encrypt plaintext
    for i in range(numRails-1, -1, -1):
        # create each rail
        for j in range(i, len(plaintext), numRails):
            ciphertext += plaintext[j]
            
    return ciphertext

def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    # set up decrypting process
    index_counter = 0
    plaintext_list = [''] * len(ciphertext)
    
    # decrypt ciphertext
    for i in range(numRails-1, -1, -1):
        # identify each rail
        for j in range(i, len(ciphertext), numRails):
            plaintext_list[j] = ciphertext[index_counter]
            index_counter += 1
            
    return ''.join(plaintext_list)

def encrypt_decrypt():
    '''encrypt_decrypt() -> None
    encrypts or decrypts a text'''
    while True:
        # get text to process
        text = ''
        while text.strip() == '':
            text = input('Enter text to either encrypt or decrypt: ')

        print()

        # choose either encryption or decryption
        choice = ''
        while choice.lower() not in ('a','b'):
            choice = input('Type \'a\' for encryption or \'b\' for decryption: ')
        
        choice = choice.lower()
        print()
        
        # encryption
        if choice == 'a':
            encrypt_key = random.randrange(2, len(text)//2+1)
            print(encipher_fence(text, encrypt_key))
            print(f'Key is {encrypt_key}')
        # decryption
        else:
            # input of decryption key
            while True:
                decrypt_key = input('Enter the key for decryption: ')
                
                # no input
                if decrypt_key.strip() == '':
                    continue
                # input is not a nonnegative integer
                elif not decrypt_key.isdigit():
                    print(f'{decrypt_key} is not a nonnegative integer.\n')
                # input is valid
                else:
                    decrypt_key = int(decrypt_key)
                    print()
                    break

            print(decipher_fence(text, decrypt_key))

        # continue using this program or not
        keep_going = ''
        while keep_going.lower() not in ('y','n'):
            keep_going = input('Do you want to continue using this device? (y/n): ')

        keep_going = keep_going.lower()
        print()

        # terminate the loop if quit
        if keep_going == 'n':
            break

encrypt_decrypt()