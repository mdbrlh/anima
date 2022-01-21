#!/usr/bin/env python3

import typing
import sys
import base64
import json

from enum import IntEnum


class Stat(IntEnum):
    STRENGTH = 0
    INTELLIGENCE = 1
    DEXTERITY = 2
    VITALITY = 3
    #HEALTH = 5
    HEALTH_REGEN = 6
    #MANA = 6
    MANA_REGEN = 7
    SPEED = 8
    PHYSICAL_DMG = 9
    MAGICAL_DMG = 10
    CRITICAL = 12
    ATTACK_SPEED = 11 # max 330
    ARMOR = 14
    MAGICAL_RES = 15
    DODGE = 19 # max 40
    GOLD_DISCOVERY = 20
    MAGICAL_DISCOVERY = 21
    LIFE_LEACH = 22
    MANA_HIT = 23    
    THORNS = 24    
    BLOCK = 25 # max 60
    

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

    def set_stat(self, stat: Stat, v: int):
        self.c['ps'][stat] = float(v)
    
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
    
    # god mode
    c = load_file(args[0])
    c.set_gold(10_000_000_000)
    c.set_oboli(10_000_000_000)
    c.set_astra(10_000_000_000)
    c.set_stat(Stat.STRENGTH, 1_000_000_000)
    c.set_stat(Stat.INTELLIGENCE, 1_000_000_000)
    c.set_stat(Stat.DEXTERITY, 1_000_000_000)
    c.set_stat(Stat.VITALITY, 1_000_000_000)
    c.set_stat(Stat.THORNS, 1_000_000_000)
    c.set_stat(Stat.BLOCK, 60)
    c.set_stat(Stat.DODGE, 40)
    c.set_stat(Stat.SPEED, 80)
    c.set_stat(Stat.CRITICAL, 100)
    c.set_stat(Stat.ATTACK_SPEED, 10_000)
    c.set_all_sorts(10_000)
    save_file(c, args[0])

if __name__ == '__main__':
    main(sys.argv[1:])

