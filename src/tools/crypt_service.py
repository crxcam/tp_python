
import string
import random


def generated_sel(value: str) -> str:
    sel: str = ''
    for el in value:
        sel += ''.join(random.choice(string.printable))
    return sel


def generated_tuple(_range_max: int) -> tuple[int]:
    value:int =_range_max
    result = []
    while value > 0:
        result.append(random.randint(1, _range_max))
        value = value - 1
    return tuple(map(int, result))


def calc_hash_value(char: str, tuple_value: int)->str:
    _ascii_number: int = ord(char) + tuple_value
    return chr(_ascii_number % 128)


def hash_password(passwors_input: str, _tuple: tuple[int]) -> str:
    password_hash: str = ''
    index: int = 0
    for el in passwors_input:
        password_hash += calc_hash_value(el, _tuple[index])
        index = index + 1
    return password_hash


def crypt(input_clear_pswd: str)-> tuple[str,int]:
    sel = generated_sel(input_clear_pswd)
    paswd_concat = input_clear_pswd+sel
    _tuple = generated_tuple(len(paswd_concat))
    password_hashed = hash_password(paswd_concat, _tuple)
    return sel, _tuple, password_hashed


def compare_password(input_pswd: str, sel: str, _tuple: tuple[int], db_passwd: str) -> bool:
    input_pswd_hashed:str = hash_password(input_pswd+sel, _tuple)
    return input_pswd_hashed == db_passwd


#crypt_result = crypt('toto87fsd')
#comp_pswd =  compare_password('toto87fsd',':\nS"9VGK1',(12, 15, 12, 15, 8, 2, 4, 6, 6, 4, 8, 12, 9, 2, 6, 3, 2, 13),'\x00~\x00~@9jyj>\x12_+;\\JM>')
# clear pswd : 'toto87fsd'
#tuple (12, 15, 12, 15, 8, 2, 4, 6, 6, 4, 8, 12, 9, 2, 6, 3, 2, 13)
#sel ':\nS"9VGK1'
#db_pass  '\x00~\x00~@9jyj>\x12_+;\\JM>'
#print('crypt result :', crypt_result)
#print('compare_password :', comp_pswd)
