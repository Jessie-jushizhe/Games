def encode(sentence, key):
    new_sentence = ""
    for letter in sentence:
        if letter == " ":
            new_sentence += " "

        elif 1 <= key <= 26:
            new_a = ord(letter)+key
            if ord('a') <= ord(letter) <= ord('z'):
                if new_a > ord('z'):
                    new_sentence += chr(new_a-26)
                else:
                    new_sentence += chr(new_a)
            elif ord('A') <= ord(letter) <= ord('Z'):
                if new_a > ord('Z'):
                    new_sentence += chr(new_a - 26)
                else:
                    new_sentence += chr(new_a)

    return new_sentence

def decode(sentence, key):
    new_sentence = ""
    for letter in sentence:
        if letter == " ":
            new_sentence += " "

        elif 1 <= key <= 26:
            new_a = ord(letter) - key
            if ord('a') <= ord(letter) <= ord('z'):
                if new_a < ord('a'):
                    new_sentence += chr(new_a + 26)
                else:
                    new_sentence += chr(new_a)
            elif ord('A') <= ord(letter) <= ord('Z'):
                if new_a < ord('A'):
                    new_sentence += chr(new_a + 26)

                else:
                    new_sentence += chr(new_a)

    return new_sentence

d_or_e = input("Do you want to encode or decode your sentence? (d/e) :")
while d_or_e != "d" and d_or_e != "e":
    d_or_e = input("Do you want to encode or decode your sentence? (d/e) :")
sentence = input("Enter your sentence: ")
while sentence.isalpha() != True:
    sentence = input("Enter your sentence: ")

key = int(input("Enter your key: "))
while key.isnumeric() != True:
    key = int(input("Enter your key: "))

if d_or_e == "d":
    print(decode(sentence, key))
elif d_or_e == "e":
    print(encode(sentence, key))