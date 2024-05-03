
import math
import string
import random


def generated_sel(value: str) -> str:
    sel: str = ''
    for el in value:
        sel += ''.join(random.choice(string.printable))
    return sel


def generated_tuple(range_max: str) -> tuple[int]:
    value: int = range_max
    result = []
    while value > 0:
        result.append(random.randint(1, range_max))
        value = value - 1
    return tuple(map(int, result))


def calc_hash_value(char: str, tuple_value: int) -> str:
    _ascii_number: int = ord(char) + tuple_value
    if _ascii_number > 127:
        _ascii_number = math.ceil(_ascii_number / 2)
        return chr(_ascii_number % 128)
    return chr(_ascii_number % 128)


def hash_password(passwors_input: str, _tuple: tuple[int]) -> str:
    password_hash: str = ''
    index: int = 0
    for el in passwors_input:
        password_hash += calc_hash_value(el, _tuple[index])
        index = index + 1
    return password_hash


def crypt(input_clear_pswd: str) -> tuple[str, int, str]:
    sel = generated_sel(input_clear_pswd)
    paswd_concat = input_clear_pswd+sel
    _tuple = generated_tuple(len(paswd_concat))
    password_hashed = hash_password(paswd_concat, _tuple)
    return sel, _tuple, password_hashed


def compare_password(input_pswd: str, salt: str, _tuple: tuple[int], db_passwd: str) -> bool:
    if len(_tuple)/2 != len(input_pswd):
        return False

    input_pswd_hashed: str = hash_password(input_pswd+salt, _tuple)
    return input_pswd_hashed == db_passwd
