#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
import base64
from Crypto.Cipher import AES
import re
from Crypto.Util.Padding import pad, unpad
import json
key = '9999912134534198'

def add_to_16(value):
    if len(value) % 16 != 0:
        value += '\x00'
        # continue
    return str.encode(value)


def decrypt(key, text):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    base64_decrypted = base64.decodebytes(key.encode())
    decrypted_text = re.sub('([^0-9\\.])', '', str(aes.decrypt(base64_decrypted)).encode())
    return decrypted_text


def get_score():
    encrypt_filename = 'score.json'
    encrypt_file = open(encrypt_filename, 'r', encoding='utf-8')
    student_id = input(b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe4\xbd\xa0\xe4\xb8\x93\xe5\xb1\x9e\xe7\x9a\x84\xe9\x9a\x8f\xe6\x9c\xba\xe6\x95\xb0\xef\xbc\x8c\xe6\x9f\xa5\xe8\xaf\xa2\xe4\xbd\xa0\xe7\x9a\x84\xe8\xaf\xa6\xe7\xbb\x86\xe6\x88\x90\xe7\xbb\xa9'.decode())
    student_id = int(student_id)
    student_id = input(b'\xe5\xad\xa6\xe5\x8f\xb7\xe8\xbe\x93\xe5\x85\xa5\xe9\x94\x99\xe8\xaf\xaf,\xe8\xaf\xb7\xe9\x87\x8d\xe6\x96\xb0\xe8\xbe\x93\xe5\x85\xa5'.decode())
    student_id = int(student_id)
    # continue

if __name__ == '__main__':
    target = '200110617'
    with open('score.json', 'r', encoding='utf-8') as f:
        while True:
            data = f.readline()
            if data is None or (data is not None and len(data) == 0):
                break
            js = json.loads(data)
            # print(js)
            for k in js:
                dec = base64.decodebytes(js[k][:-1].encode())
                aes = AES.new(add_to_16(key), AES.MODE_ECB)
                val = re.sub('([^0-9\\.])', '', aes.decrypt(dec).decode())
                js[k] = val
                # print(f"{k}: {val}")
            if js['学号'] == target:
                print(js)
    # print(decrypt(key))
    # get_score()
    # x = input()
