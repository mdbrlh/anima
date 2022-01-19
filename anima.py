#!/usr/bin/env python3

import typing
import sys
import base64
import json


class Char:
    def __init__(self, char: dict):
        self.c = char
    
    def set_level(self, v: int):
        self.c['l'] = v

    def set_exp(self, v: int):
        self.c['e'] = v

    def set_gold(self, v: int):
        self.c['g'] = v    

    def set_oboli(self, v: int):
        self.c['cs'] = v
    
    def set_astra(self, v: int):
        self.c['ec'] = v

    def set_keys(self, v: int):
        self.c['lk'] = v

    def set_strength(self, v: float):
        self.c['ps'][0] = v
    
    def set_intelligence(self, v: float):
        self.c['ps'][1] = v
    
    def set_dexterity(self, v: float):
        self.c['ps'][2] = v
    
    def set_vitality(self, v: float):
        self.c['ps'][3] = v
    
    def set_speed(self, v: float):
        """default is 30"""
        self.c['ps'][8] = v

    def set_critical(self, v: float):
        self.c['ps'][12] = v
    
    def set_spell_points(self, v: int):
        self.c['ap'] = v

    def set_char_points(self, v: int):
        self.c['sp'] = v
    
    def set_all_sorts(self, v: int):
        """set all sorts to the value"""
        self.c['al'] = [v for p in self.c['al']]


def load_file(filename: str) -> Char:
    '''load the file as bytes and extract the json'''
    with open(filename, 'rb') as f:
        r = f.read()
    json_bytes = base64.b64decode(r[24:-1])
    char_dict = json.loads(json_bytes)
    return Char(char_dict)


def save_file(char: Char, filename: str):
    '''save file as .char'''
    json_bytes = bytes(json.dumps(char.c), 'utf8')
    jb = base64.b64encode(json_bytes)

    # calculate the length of the base64ed json (ugly.. but working)  
    bin_len = bin(len(jb))   
    p = '0' * (8 - len(bin_len[2:-7])) 
    b = '1' + bin_len[-7:] + p + bin_len[2:-7]
    length = bytes([int(b[0:8], 2), int(b[8:], 2)])
    
    content = b'\x00\x01\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x06\x01\x00\x00\x00' + length + jb + b'\x0b'

    with open(filename, 'wb') as f:
        f.write(content)


def main(args):
    if not args:
        print('Usage: anima.py <name.char>')
        return
    
    # semi god mode
    c = load_file(args[0])
    c.set_gold(9_999_999_999)
    c.set_oboli(9_999_999_999)
    c.set_astra(9_999_999_999)
    c.set_strength(9_999_999.0)
    c.set_intelligence(9_999_999.0)
    c.set_dexterity(9_999_999.0)
    c.set_vitality(9_999_999.0)
    c.set_speed(75)
    c.set_critical(100)
    c.set_all_sorts(9999)
    save_file(c, args[0])

if __name__ == '__main__':
    main(sys.argv[1:])

