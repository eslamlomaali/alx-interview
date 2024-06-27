#!/usr/bin/python3
""" UTF-8 Validation module """


def validUTF8(data):
    """
    Method that determines if a the data is represents a valid
    UTF-8 encoding.
    """
    n_b = 0

    m = 1 << 7
    n = 1 << 6

    for x in data:

        m_b = 1 << 7

        if n_b == 0:

            while m_b & x:
                n_b += 1
                m_b = m_b >> 1

            if n_b == 0:
                continue

            if n_b == 1 or n_b > 4:
                return False

        else:
            if not (x & m and not (x & n)):
                    return False

        n_b -= 1

    if n_b == 0:
        return True

    return False
