# Copyright 2022 by Néstor Nahuatlato
# <soy_nestor@hotmail.com>
# Licensed under GNU General Public License 3.0 or later.
# @license GPL-3.0+

import re
from os import system, name
from time import sleep

# Numeric system rules
pattern_bin = '0b[0,1]'
pattern_oct = '0o[0-7]'
pattern_hex = '0x[0-9,a-f]'

# Binary, Octal and Hexadecimal prefixes
bin_prefix = '0b'
oct_prefix = '0o'
hex_prefix = '0x'

# Auxliary constants
C_0 = 0
C_1 = 1
C_2 = 2
C_8 = 8
C_10 = 10
C_16 = 16
C_20 = 20

EXIT = 'e'
BINARY = "BINARY"
OCTAL = "OCTAL"
DECIMAL = "DECIMAL"
HEXADECIMAL = "HEXADECIMAL"
ERROR = "You've typed an invalid number"
empty_string = ""

WINDOWS = 'nt'

def clear():
    if  name == WINDOWS:
        _ = system("cls")
    else:
        _ = system("clear")

def user_guide():
    print(">" * C_20)
    print("Type a number following any of these rules.\n")
    print(f"{DECIMAL}: from 0 to 9")
    print(f"{BINARY} ({bin_prefix}): 0 and 1")
    print(f"{OCTAL} ({oct_prefix}): from 0 to 7")
    print(f"{HEXADECIMAL} ({hex_prefix}): from 0 to 9 and from 'a' to 'f'\n")
    print(f"Exit: '{EXIT}'")
    print("<" * C_20)

def check(string, pattern, base):
    result = string.isdecimal() if base == C_10 else re.match(pattern, string)

    if result:
        show_values(string, base)
    else:
        print(ERROR)

def show_values(string, base):
    aux_int = int(string, base)

    print(f"BIN {bin(aux_int)}")
    print(f"OCT {oct(aux_int)}")
    print(f"DEC {aux_int}")
    print(f"HEX {hex(aux_int)}")

def main():
    clear()

    while True:
        user_guide()
        string = input()
        string = string.lower()

        if string == EXIT:
            break
        else:
            clear()
            string_size = len(string)
            
            if string_size == C_1:
                check(string, empty_string, C_10)
            elif string_size >= C_2:
                user_prefix = string[C_0:C_2]

                if user_prefix == bin_prefix:
                    check(string, pattern_bin, C_2)
                elif user_prefix == oct_prefix:
                    check(string, pattern_oct, C_8)
                elif user_prefix == hex_prefix:
                    check(string, pattern_hex, C_16)
                else:
                    check(string, empty_string, C_10)
            else:
                print("Wrong input...")
                sleep(C_2)
                clear()

if __name__ == "__main__":
    main()