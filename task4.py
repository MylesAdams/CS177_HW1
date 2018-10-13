#!/usr/bin/env python3

from Crypto.Cipher import AES
import binascii
import os

def PartA() -> None:
    print('Part B')
    PartAKey = b'\x10\x04\x20\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    PartAPlainText = b'\x10\x04\x20\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    PartAEncryptor = AES.new(PartAKey, AES.MODE_ECB)
    PartACipherText = PartAEncryptor.encrypt(PartAPlainText)
    PartARecoveredPlainText = PartAEncryptor.decrypt(PartACipherText)

    print('Key :', binascii.hexlify(PartAKey))
    print('Cipher Text:', binascii.hexlify(PartACipherText))
    print('Recovered Plain Text:', binascii.hexlify(PartARecoveredPlainText), '\n')


def PartB() -> None:
    print('Part B')
    PartBKey = b'\x10\x04\x20\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    PartBEncryptor = AES.new(PartBKey, AES.MODE_ECB)
    for i in range(0, 10000):
        PartBPlainText = os.urandom(16)
        PartBCipherText = PartBEncryptor.encrypt(PartBPlainText)

        if binascii.hexlify(PartBCipherText)[-2:] == b'00':
            print('Message :', binascii.hexlify(PartBPlainText))
            print('Cipher Text :', binascii.hexlify(PartBCipherText), '\n')
            break

def PartC() -> None:
    print('Part C')
    PartCPlainText = b'\x10\x04\x20\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    for i in range(0, 10000):
        PartCKey = os.urandom(16)
        PartCEncryptor = AES.new(PartCKey, AES.MODE_ECB)
        PartCCipherText = PartCEncryptor.encrypt(PartCPlainText)

        if binascii.hexlify(PartCCipherText)[-2:] == b'00':
            print('Key :', binascii.hexlify(PartCKey))
            print('Cipher Text :', binascii.hexlify(PartCCipherText))
            break


if __name__ == "__main__":
    PartA()
    PartB()
    PartC()
