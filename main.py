alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotoropt=["EMSADNQPJWGCIZKOTLHUFYBVXR",#1
          "LBNSIXPZKAMECOVDRHTYUWGFJQ",#2
          "KGQWXITYPUROBDJVAFCMLHENSZ",#3
          "TKBFUXORLSACVHNYJIZQPWDEGM",#4
          "WYNLAEHVJKFIPQBXZTUCGSMORD",#5
          "ZETKLGHCXOVNBPAYUIQFSWJMDR",#6
          "QASMODBWTNLEFXRPHKICVUGJYZ",#7
          "FITNGJQKCHSVYZXEMLURBWAOPD"#8
         ]
reflector="UKNEDTQFBRPOXWYZVSAGJLIMHC"

def getpair(letter, pairset):
  for count in range(len(pairset)):
    if pairset[count] == letter:
      if count%2 == 0:
        return pairset[count+1]
      else:
        return pairset[count-1]
  return letter
        
def shiftRotor(rotor, amount):
  newRotor = ""
  for l in range(len(rotor)):
    newRotor += rotor[(l+amount)%len(rotor)]
  return newRotor
  
def stepRotors(keys):
  keys[0]+=1
  keys[0]%=26
  if keys[0]==0:
    keys[1]+=1
    keys[1]%=26
    if keys[1]==0:
      keys[2]+=1
      keys[2]%=26
  return keys
    
def cipher(text, key):
  keys = [*key.upper().split()[1]]
  rotorarrangement = key.split()[0]
  plugs = ""
  if len(key.upper().split())>=3:
    plugs = key.upper().split()[2]
  rotors = []
  for rotor in rotorarrangement:
    rotors.append(rotoropt[int(rotor)-1])
  
  keys[0] = alphabet.index(keys[0])
  keys[1] = alphabet.index(keys[1])
  keys[2] = alphabet.index(keys[2])
  text = text.upper()
  results = ""
  for letter in text:
    letter = getpair(letter, plugs)
    if letter in alphabet:
      a = alphabet.index(shiftRotor(rotors[0], keys[0])[alphabet.index(letter)])
      b=shiftRotor(rotors[2],keys[2])[alphabet.index(shiftRotor(rotors[1],keys[1])[a])]
      c = getpair(b, reflector)
      d = shiftRotor(rotors[0],keys[0]).index(alphabet[shiftRotor(rotors[1],keys[1]).index(alphabet[shiftRotor(rotors[2], keys[2]).index(c)])])
      e = alphabet[d]
      e = getpair(e, plugs)
      results += e
    else:
      results += letter
    keys = stepRotors(keys)
  return results 
    
print("Based on the German Engima Machine")
print(cipher(input("Enter text\n"),input("Enter key (num num num [space] letter letter letter [space] plugboard pairs)\n")))
