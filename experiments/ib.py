def ib(i, length):
    # i - integer to convert to bytes
    # length - desired length of the byte object
    byte_representation = bytearray()
    # print(byte_representation)
    for n in range(length):
        byte = (i >> (n * 8)) & 0xFF
        byte_representation.append(byte)
    print(byte_representation[::-1])
    return bytes(byte_representation[::-1])


ib(6382147, len(str(6382147)))
