''' simple code to generate a api_key '''
import random
import string

def generate_key(length: int) -> str:
    ''' function to generate random string (letters + digits) of any length'''
    _tt = [random.choice(list(string.ascii_letters) + list(string.digits)) for _ in range(length)]
    print(_tt)
    return ''.join(_tt)


if __name__ == '__main__':
    print(generate_key(32))
