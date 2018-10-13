#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii
import os

Counter = Counter.new(128, initial_value=int(binascii.hexlify(os.urandom(16)), 16))
Encryptor = AES.new(os.urandom(16), AES.MODE_CTR, counter=Counter)


