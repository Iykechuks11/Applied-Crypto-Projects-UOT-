def bi(b):
    # b - byte to encode as an integer
    int_val = 0
    for byte in b:
        # print(byte)
        int_val = (int_val << 8) | byte
    print(int_val)
    return int_val


bi(b'0\xad\xa4\xf6\xf4d')
