import asn1

encoder = asn1.Encoder()
encoder.start()
encoder.write(False, asn1.Numbers.Boolean)
encoded_bytes = encoder.output()

print(encoded_bytes)
