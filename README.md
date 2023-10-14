# encode-decode
Based on the German **Enigma machine** used in WWII. As this cipher is self-reciprocal, the same function can be used to encode and decode.
## how to use
To use, enter your input of either plaintext of ciphertext. Then, enter your key. The same key will be used for encryption and decryption, and it is highly unlikely that a different key will yield the same results.
## keys
The program takes in an input, either plaintext or ciphertext, and a key. This key is what tells the program how to cipher the text.
### key format
>
> num num num \[space] letter letter letter \[space] plugboard combinations
> 
The *num* entries shall be a number, one through eight, which shall represent the order of the rotors used.
The *letter* entries shall be a letter of the alphabet, A through Z, which shall represent the starting rotation of the rotors.
Finally, the plugboard combinations shall be pairs of letters, such as UF or AU. While you can put up to 13 of these, combinations sharing a letter should not be used together, as it may break the program.
An example key is shown below:
>
> 635 HWC PDJCBTESUKML 
>
Make sure that the plugboard combinations contains an even number of letters, and that there are no duplicates.
