#!/usr/bin/env python3

import asn1
import sys


def asn1_boolean(boolean):
    """
    Input: true/false.
    Output: Data encoding of true or false
    """
    encoder = asn1.Encoder()
    encoder.start()
    encoder.write(boolean, asn1.Numbers.Boolean)
    encoded_bytes = encoder.output()

    # return encoded_bytes
    # print(encoded_bytes)
    with open('true.der', 'wb') as t:
        t.write(encoded_bytes)
        t.close()


def usage():
    print("Usage:")
    print("asn1_boolean <True/False>")
    # print("decrypt <ciphertext file> <key file> <plaintext output file>")
    sys.exit(1)


if len(sys.argv) != 2:
    usage()
elif sys.argv[1] == "True":
    asn1_boolean(sys.argv[1])
elif sys.argv[1] == "False":
    asn1_boolean(sys.argv[1])
else:
    usage()
