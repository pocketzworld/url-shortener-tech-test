# modified from here: https://stackoverflow.com/questions/1119722/base-62-conversion

_alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(num) -> str:
    """Encode a positive number into Base X and return the string.

    Arguments:
    - `num`: The number to encode
    """
    if num == 0:
        return _alphabet[0]
    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    _divmod = divmod  # Access to locals is faster.
    base = len(_alphabet)
    while num:
        num, rem = _divmod(num, base)
        arr_append(_alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def decode(encoded) -> int:
    """Decode a Base X encoded string into the number

    Arguments:
    - `encoded`: The encoded string
    """
    base = len(_alphabet)
    strlen = len(encoded)
    num = 0

    idx = 0
    for char in encoded:
        power = (strlen - (idx + 1))
        num += _alphabet.index(char) * (base ** power)
        idx += 1
    return num