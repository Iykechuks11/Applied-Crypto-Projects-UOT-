# https: // cs.stackexchange.com/questions/95442/bytes-from -integer-using-bitwise-operators
import os


def bi(b):
    # b - byte to encode as an integer
    int_val = 0
    for byte in b:
        # print(byte)
        int_val = (int_val << 8) | byte
        # print(int_val)
    return int_val


def ib(i, length):
    # i - integer to convert to bytes
    # length - desired length of the byte object
    byte_representation = bytearray()
    # print(byte_representation)
    for n in range(length):
        byte = (i >> (n * 8)) & 0xFF
        byte_representation.append(byte)
        # print(byte_representation)
    return bytes(byte_representation[::-1])


# def encrypt(p):
#     """
#     Encrypts plaintext

#     Convert plaintext bytes to one big integer
#     Obtain random key the same length as plaintext (use os.random())
#     Convert key bytes to one big integer
#     # Read the plaintext file content into bytes object
#     XOR plaintext and key integers
#     Saves the key, and saves the result to file
#     Use bitwise operations
#     """

#     plaintext_int = bi(p)
#     # print(plaintext_int)

#     # # obtain random key the same length as plaintext
#     len_ptext = len(str(plaintext_int))
#     print(f"The length of the plaintext: {len_ptext}")
#     random_key = os.urandom(len_ptext)
#     print(f"The random key generated: {random_key}")
#     print(f"The length of the random key: {len(random_key)}")
#     random_key_int = bi(random_key)
#     # # print(f"The random key converted to integer is {random_key_int}")

#     # # ensure that length is same
#     # assert len(plaintext_byte) == len(
#     #     random_key), "Key length does not match plaintext length"

#     # # xor plaintext and random key
#     ciphertext_int = plaintext_int ^ random_key_int
#     print(f"plaintext xored with key = ciphertext_int: {ciphertext_int}")

#     # # convert ciphertext integer back to bytes
#     ciphertext_byte = ib(ciphertext_int, len_ptext)
#     print(f"Ciphertext (bytes): {ciphertext_byte}")


# bi = bi(b'abc')
# print(f"From byte to int: {bi}")

# ib = ib(6382179, len(str(6382179)))
# print(f"Fron int to byte: {ib}")

# c = encrypt(b'abc')
# print(f"Encrypted data: {c}")

def decrypt(c, k):
    # print(c)
    # print(k)
    ctext_int = bi(c)
    print(f"Ciphertext to int: {ctext_int}")

    key_int = bi(k)
    print(f"Key to int: {key_int}")

    p_maybe = ctext_int ^ key_int
    print(f"Maybe this is the plaintext: {p_maybe}")

    p_maybe_byte = ib(p_maybe, len(str(p_maybe)))
    print(f"Maybe plaintext to byte: {p_maybe_byte}")


decrypt(b'\xe4\xf1\xf1\xc4\x05\xd5\xe8', b'\xe4\xf1\xf1\xc4d\xb7\x8b')
