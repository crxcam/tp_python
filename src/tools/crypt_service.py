
import string
import random


def generated_sel(value: str) -> str:
    sel: str = ''
    for el in value:
        sel += ''.join(random.choice(string.printable))
    return sel


def generated_tuple(value: int) -> tuple[int]:
    _range_max = value
    result = []
    while value > 0:
        result.append(random.randint(1, _range_max))
        value = value - 1
    return tuple(map(int, result))


def calc_hash_value(char: str, tuple_value: int):
    _ascii_number: int = ord(char) + tuple_value
    return chr(_ascii_number % 128)


def hash_password(passwors_input: str, _tuple: tuple[int]) -> str:
    password_hash: str = ''
    index: int = 0
    for el in passwors_input:
        password_hash += calc_hash_value(el, _tuple[index])
        index = index + 1
    return password_hash


def crypt(input_clear_pswd: str):
    sel = generated_sel(input_clear_pswd)
    paswd_concat = input_clear_pswd+sel
    _tuple = generated_tuple(len(paswd_concat))
    password_hashed = hash_password(paswd_concat, _tuple)
    return sel, _tuple, password_hashed


crypt_result = crypt('toto87fsd')
print('crypt result :', crypt_result)
