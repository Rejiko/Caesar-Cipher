alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(text,shift,direction):
    new_text = ""
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char)
            if direction == "decode":
                new_text += alphabet[pos-shift]
            elif direction == "encode":
                new_text += alphabet[pos+shift]
        else:
            new_text += char
    print(new_text)

end_of_program = False
while not end_of_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction in ["encode", "decode"]:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift %= 26
        caesar(text, shift, direction)
        again = input("Type 'yes' if you want to again. Otherwise type 'no'.\n")
        if again == "yes":
            print("\n")
        else:
            end_of_program = True
    else:
        print("Invalid input. Please try again.\n")