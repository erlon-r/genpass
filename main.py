import secrets
from random import sample
from string import digits, punctuation, ascii_lowercase, ascii_uppercase


def get_char(string: str) -> str:
    """Returns a random character from a string."""
    return secrets.choice(string)


def remove_spaces(string: str) -> str:
    """Removes all spaces contained in the string."""
    return string.replace(' ', '')


def remove_chars(string: str) -> str:
    """Returns a string with all ASCII characters except those included in the string parameter."""
    chars = list(f'{digits} {punctuation} {ascii_lowercase} {ascii_uppercase}')
    for char in remove_spaces(string):
        if char in chars:
            chars.remove(char)
    return ''.join(chars).strip()


def print_header_error() -> None:
    """Prints the header of an error message."""
    color_red = '\033[31m'
    color_end = '\033[0m'
    print(f'genpass: {color_red}error{color_end}:', end=' ')


def make_password(chars: list, length: int) ->  str:
    """Returns a string of random characters."""
    password = []
    count = 0
    for i in range(length):
        if count > len(chars)-1:
            random_index = secrets.randbelow(len(chars))
            password.append(get_char(chars[random_index]))
        else:
            password.append(get_char(chars[count]))
        count += 1
    return ''.join(sample(password, k=len(password)))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        prog='genpass',
        description='password generator',
        epilog='Developer by Erlon'
    )

    parser.add_argument(
        '-l',
        type=int,
        default=20,
        metavar='INT',
        help='password length (dafault 20)'
    )

    parser.add_argument(
        '-e',
        type=str,
        default='',
        metavar='STR',
        help='characters to exclude from password'
    )

    args = parser.parse_args()

    chars = remove_chars(args.e).split()

    print_password = True

    if len(chars) != 4:
        print_password = False
        print_header_error()
        print('a strong password needs numbers, symbols ' \
              'upper and lower case letters.')

    if args.l < 8:
        print_password = False
        print_header_error()
        print('a strong password must contain at least 8 characters.')

    if print_password:
        print(make_password(chars, args.l))
