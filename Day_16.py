f = open('Day_16_Input.txt', 'r')
x = f.read().strip()
binTransmission = bin(int(x, 16))[2:].zfill(len(x) * 4)
# print(len(binTransmission))
# print(binTransmission)
# print(binTransmission)
# while len(binTransmission) > 0:
# version = int(binTransmission[0:3], 2)
# typeID = int(binTransmission[3:6], 2)
versionTotal = 0
while int(binTransmission, 2) != 0:
    print(binTransmission)
    version = int(binTransmission[0:3], 2)
    typeID = int(binTransmission[3:6], 2)
    versionTotal += version
    if typeID == 4:
        prefix = 6
        while True:
            if binTransmission[prefix] == 1:
                prefix += 4
            else:
                break 

        # first = binTransmission[7:11]
        # second = binTransmission[12:16]
        # third = binTransmission[17:21]
        # binLitValue = first + second + third
        # endOfPacketIndex = 21
        # print(int(binLitValue, 2))
    else:
        lengthTypeID = binTransmission[6]
        # print(lengthTypeID)
        if lengthTypeID == '0':
            subPacketLength = binTransmission[7:22]
            print('sub', subPacketLength)
            lengthTypeID = 22 + int(subPacketLength, 2)
            subPacket = binTransmission[22:lengthTypeID]
            print(subPacket)
            endOfPacketIndex = lengthTypeID
            print('dank')
        else:
            numSubPackets = int(binTransmission[7:18], 2)
            endOfPacketIndex = (numSubPackets * 11) + 18
            sub1 = int(binTransmission[18:29], 2)
            sub2 = int(binTransmission[29:40], 2)
            sub3 = int(binTransmission[40:51], 2)
    print(len(binTransmission), endOfPacketIndex)
    binTransmission = binTransmission[endOfPacketIndex:]
    print(binTransmission)
    # print(versionTotal)
print(versionTotal)
    


# print(version, typeID)    
# 110100010100101001000100100
# 110100010100101001000100100

# 000000000011011
# 000000001101111
# 00111000000000000110111101000101001010010001001000000000
# 00111000000000000110111101000101001010010001001000000000



# print(hex(int('1101', 2)))
# # 110100101111111000101000
# # 110100101111111000101000
# print(int('000000000011011', 2))
# binPacket = bin(int('EE00D40C823060', 16))[2:]
# packetVersion = binPacket[:3]
# packetTypeID = binPacket[3:6]
# numSubPackets = binPacket[7:18]
# print(packetVersion, packetTypeID)
# print(numSubPackets)
# print(int(numSubPackets, 2))
# #00111000000000000110111101000101001010010001001000000000
# #0b111000000000000110111101000101001010010001001000000000