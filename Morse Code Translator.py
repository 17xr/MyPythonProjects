English_To_Morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

Morse_To_English = {}
for letter, key in English_To_Morse.items():
    Morse_To_English[key] = letter


def encoder(message):
    message = message.upper()
    encrypted = ''
    for letter in message:
        if letter != ' ':
            encrypted += English_To_Morse[letter] + ' '
        else:
            encrypted += '/'
    return encrypted


def decoder(message):
    message = message.split('/')
    decrytped = ''
    for word in message:
        word = word.split(' ')
        for char in word:
            if char != '':
                decrytped += Morse_To_English[char]
        decrytped += ' '
    return decrytped


print("Welcome to Morse code decoder/encoder !")
def main():
    while True:
        try:
            choice = int(input("Enter a num to proceed (1 for encoding / 2 for decoding) : "))
            if choice == 1 or choice == 2:
                break
        except:
            print("Please enter a number !")

    if choice == 1:
        print('Enter the message u want to encrypt in Morse code : ')
        msg = str(input('>>> '))
        morse = encoder(msg)
        print('### Morse code of your message is: ###')
        print(morse)

    elif choice == 2:
        print('Enter the Morse code u want to decrypt: ')
        msg = str(input('>>> '))
        text = decoder(msg)
        print('### English text of your Morse code is ###')
        print(text)

if __name__ == '__main__':
    main()