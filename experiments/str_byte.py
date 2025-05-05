# byte to int
def bi(b):
    # b - byte to encode as an integer
    int_val = 0
    for byte in b:
        print(byte)
        int_val = (int_val << 8) | byte
        print(bin(int_val))
        print(int_val)
    return int_val


# int to byte
def ib(i):
    # b - byte to encode as an integer
    binary = bin(i)
    print(len(binary))
    print(binary[:-1])
    pass
    # int_val = 0
    # for byte in b:
    #     print(byte)
    #     int_val = (int_val << 8) | byte
    #     print(int_val)
    # return int_val


bi = bi(b'abC')
print(bi)
ib(bi)

i = 6382147
print(i >> 0 & 0xFF)  # gives the last 8 digit letter 67
print(i >> 8 & 0xFF)  # 98
print(i >> 16 & 0xFF)  # 97
print(i >> 24 & 0xFF)  # 0
