#!/usr/bin/python3
# https://docs.python.org/3/library/operator.html
import os
import sys


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


def encrypt(pfile):
    """
    Encrypts plaintext

    Convert plaintext bytes to one big integer
    Obtain random key the same length as plaintext (use os.random())
    Convert key bytes to one big integer
    # Read the plaintext file content into bytes object
    XOR plaintext and key integers
    Saves the key, and saves the result to file
    Use bitwise operations
    """
    try:
        with open(pfile, 'rb') as f_plain:
            plaintext_byte = f_plain.read()
            # print("The context of the opened file:")
            # print(plaintext_byte)

            # convert plaintext bytes to one big integer
            plaintext_byte_int = bi(plaintext_byte)
            # print(f"The plaintext converted to integer is {plaintext_byte_int}")

            # obtain random key the same length as plaintext
            len_ptext = len(plaintext_byte)
            # print(f"The length of the plaintext: {len_ptext}")
            random_key = os.urandom(len_ptext)
            # print(f"The random key generated: {random_key}")
            # print(f"The length of the random key: {len(random_key)}")
            random_key_int = bi(random_key)
            # print(f"The random key converted to integer is {random_key_int}")

            # ensure that length is same
            assert len(plaintext_byte) == len(
                random_key), "Key length does not match plaintext length"

            # xor plaintext and random key
            ciphertext_int = plaintext_byte_int ^ random_key_int
            print(f"plaintext xored with key: {ciphertext_int}")

            # convert ciphertext integer back to bytes
            ciphertext_byte = ib(ciphertext_int, len_ptext)
            print(f"Ciphertext (bytes): {ciphertext_byte}")

            # save the key to the key file
            with open("kfile", 'wb') as f_key:
                f_key.write(random_key)
            # print(f"Key saved to: {kfile}")

            # save the ciphertext to the ciphertext file
            with open("cfile", 'wb') as f_cipher:
                f_cipher.write(ciphertext_byte)
            # print(f"Ciphertext saved to: {cfile}")

    except FileNotFoundError:
        print(f"Error: Plaintext file '{pfile}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during encryption: {e}")
        sys.exit(1)


def decrypt(cfile, kfile, pfile):
    # convert cfile, kfile from byte to int
    cfile_int = bi(cfile)
    kfile_int = bi(kfile)
    # xor cfile and kfile
    p = cfile_int ^ kfile_int
    assert p == pfile, "Decryptor error"
    return pfile


c = encrypt("file.plain")
p = decrypt("cfile", "kfile", "file.plain")
