byteList = list()

with open('plain.txt') as file:
    for line in file:
        key = ''
        phrase = ''
        byte = ''
        count = 0

        for bit in line:
            byte += bit

            count += 1
            if count == 8:
                byteList.append(int(byte, 2))
                byte = ''
                count = 0

#print (byteList)

key = 78

accept = False

while not accept:
    decodedList = list()

    for byte in byteList:
        decodedValue = byte ^ key
        decodedList.append(decodedValue)

    for decodedValue in decodedList:
        print(chr(decodedValue), end=" ")
    input('Is this correct? ')
        #accept = True

    key += 1