var alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var rotoropt=["EMSADNQPJWGCIZKOTLHUFYBVXR",//1
          "LBNSIXPZKAMECOVDRHTYUWGFJQ",//2
          "KGQWXITYPUROBDJVAFCMLHENSZ",//3
          "TKBFUXORLSACVHNYJIZQPWDEGM",//4
          "WYNLAEHVJKFIPQBXZTUCGSMORD",//5
          "ZETKLGHCXOVNBPAYUIQFSWJMDR",//6
          "QASMODBWTNLEFXRPHKICVUGJYZ",//7
          "FITNGJQKCHSVYZXEMLURBWAOPD"//8
         ];
var reflector="UKNEDTQFBRPOXWYZVSAGJLIMHC";

function getpair(letter, pairset){
  for (var count = 0; count < pairset.length; count++){
    if (pairset[count] == letter){
      if (count%2 == 0){
        return pairset[count+1];
      }
      else{
        return pairset[count-1];
      }
    }
  }
  return letter;
}

function shiftRotor(rotor, amount){
  var newRotor = "";
  for (var l = 0; l < rotor.length; l++){
    newRotor += rotor[(l+amount)%rotor.length];
  }
  return newRotor;
}
  
function stepRotors(keys){
  keys[0]+=1;
  keys[0]%=26;
  if (keys[0]==0){
    keys[1]+=1;
    keys[1]%=26;
    if (keys[1]==0){
      keys[2]+=1;
      keys[2]%=26;
    }
  }
  return keys;
}
function cipher(text, key){
  var keys = key.toUpperCase().split(" ")[1].split("");
  var rotorarrangement = key.split(" ")[0];
  var plugs = "";
  if (key.toUpperCase().split(" ").length>=3){
    plugs = key.toUpperCase().split(" ")[2];
  }
  var rotors = [];
  for(var rotori = 0; rotori < rotorarrangement.length; rotori++){
    var rotor = rotorarrangement[rotori];
    rotors.push(rotoropt[parseInt(rotor)-1]);
  }
  keys[0] = alphabet.indexOf(keys[0]);
  keys[1] = alphabet.indexOf(keys[1]);
  keys[2] = alphabet.indexOf(keys[2]);
  var text = text.toUpperCase();
  var results = "";
  for (var letteri = 0; letteri < text.length; letteri++){
    var letter = text[letteri];
    letter = getpair(letter, plugs);
    if (alphabet.includes(letter)){
      var a = alphabet.indexOf(shiftRotor(rotors[0], keys[0])[alphabet.indexOf(letter)]);
      var b=shiftRotor(rotors[2],keys[2])[alphabet.indexOf(shiftRotor(rotors[1],keys[1])[a])];
      var c = getpair(b, reflector);
      var d = shiftRotor(rotors[0],keys[0]).indexOf(alphabet[shiftRotor(rotors[1],keys[1]).indexOf(alphabet[shiftRotor(rotors[2], keys[2]).indexOf(c)])]);
      var e = alphabet[d];
      e = getpair(e, plugs);
      results += e;
    }
    else{
      results += letter;
    }
    keys = stepRotors(keys);
  }
  return results 
}
