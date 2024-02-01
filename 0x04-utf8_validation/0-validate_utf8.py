#!/usr/bin/python3
"""module for UTF-8 Validation"""


def validUTF8(data):
    """method that determines if a given data set represents
    a valid UTF-8 encoding"""
    """Initialize a variable to store the number of
    bytes in the current character"""
    n_bytes = 0
    # Iterate over the list of integers
    for num in data:
        """ Get the binary representation of the integer,
        padded with zeros to 8 bits"""
        bin_rep = format(num, '#010b')[-8:]
        # If this is the first byte of a character
        if n_bytes == 0:
            # Count the number of leading 1 bits
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1
            # If the number of bytes is 0, this is a 1-byte character
            if n_bytes == 0:
                continue
            """ If the number of bytes is 1 or more than 4,
            this is an invalid byte"""
            if n_bytes == 1 or n_bytes > 4:
                return False
        # If this is a continuation byte
        else:
            # Check that the first two bits are 10
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        # Decrement the number of bytes by 1
        n_bytes -= 1
    # Check that the number of bytes is 0 at the end of the iteration
    return n_bytes == 0
