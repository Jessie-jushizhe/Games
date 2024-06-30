def encode(sentence, key):
    new_sentence=""
    for l in sentence:
        if l==" ":
            new_sentence+=" "

        elif 1<=key<=26:
            new_a=ord(l)+key
            if new_a>ord('z'):
                new_sentence+=chr(new_a-26)

            else:
                new_sentence+=chr(new_a)

    return new_sentence

def decode(sentence, key):
    new_sentence = ""
    for l in sentence:
        if l == " ":
            new_sentence += " "

        elif 1 <= key <= 26:
            new_a = ord(l) - key
            if new_a < ord('a'):
                new_sentence += chr(new_a + 26)

            else:
                new_sentence += chr(new_a)

    return new_sentence

d_or_e=input("Do you want to encode or decode your sentence? (d/e) :")

if d_or_e == "d":
    sentence=input("Enter your sentence: ")
    key=int(input("Enter your key: "))
    print(decode(sentence, key))

if d_or_e == "e":
    sentence=input("Enter your sentence: ")
    key=int(input("Enter your key: "))
    print(encode(sentence, key))

