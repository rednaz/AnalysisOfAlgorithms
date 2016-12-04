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

key = 0
#key = 110

accept = False

while not accept:
    decodedList = list()
    decodedCharList = list()

    complete = True

    print ("key = " + str(key))

    for byte in byteList:
        decodedValue = byte ^ key

        if (decodedValue < 32 and decodedValue != 10) or decodedValue > 122 or (decodedValue > 59 and decodedValue < 65):
            complete = False
            break
        decodedList.append(decodedValue)
        decodedCharList.append(chr(decodedValue))

    if not complete:
        key += 1
        continue

    for decodedValue in decodedCharList:
        print(decodedValue, end="")

    accept = True