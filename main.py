import sys

print('Enigma Machine Simulator')

bruteforced = False

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Rotors, but with shift
rotor1 = [0, 9, 3, 10, 118, 8, 17, 20, 23, 1, 11, 7,
          22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
rotor2 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25,
          13, 24, 4, 8, 22, 6, 0, 10, 112, 20, 18, 16, 14]
rotor3 = [4, 18, 14, 21, 15, 25, 9, 0, 24, 116, 20, 8,
          17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]

rotorIndexes = [-1, -1, -1]

reflector_b = [4, 13, 10, 16, 0, 20, 24, 22, 9, 8, 2, 14,
               15, 1, 11, 12, 3, 23, 25, 21, 5, 19, 7, 17, 6, 18]
reflector_c = [5, 18, 14, 10, 0, 13, 20, 4, 17, 7, 12, 1,
               19, 8, 24, 2, 22, 11, 16, 15, 25, 23, 21, 6, 9, 3]

messageInNumbers = []

while not bruteforced:
    encryptedMessage = []

    message = input(str('Enter a message to encrypt: '))
    message = message.upper()

    for i in range(0, len(rotorIndexes)):
        while rotorIndexes[i] < 0 or rotorIndexes[i] > 25:
            rotorIndexes[i] = int(input(f'Enter rotor {i+1} index (0-25): '))
            
            if rotorIndexes[i] < 0 or rotorIndexes[i] > 25:
                print('Invalid index!')

    for letter in message:
        for i in range(0, len(alphabet)):
            if letter == alphabet[i]:
                messageInNumbers.append(i)

    # Convert letter to number
    print(f'Message: {message}.\nNumbers: {messageInNumbers}.')

    for numberLetter in messageInNumbers:
        numberLetter = numberLetter + rotor1[rotorIndexes[0]]
        numberLetter = numberLetter + rotor2[rotorIndexes[1]]
        numberLetter = numberLetter + rotor3[rotorIndexes[2]]

        
        # Convert number to letter and handle overflow
        for i in range(0, len(alphabet)):
            if numberLetter == i:
                encryptedMessage.append(alphabet[i])
            elif numberLetter > 25:
                numberLetter = numberLetter - 26
                if numberLetter == i:
                    encryptedMessage.append(alphabet[i])

        rotorIndexes[0] = rotorIndexes[0] + 1

        if rotor1[rotorIndexes[0]] > 100:
            rotorIndexes[1] = rotorIndexes[1] + 1
        if rotor2[rotorIndexes[1]] > 100:
            rotorIndexes[2] = rotorIndexes[2] + 1
        if rotorIndexes[0] == 25:
            rotorIndexes[0] = 0
        if rotorIndexes[1] == 25:
            rotorIndexes[1] = 0
         
    print(f'Encrypted message: {encryptedMessage}.')