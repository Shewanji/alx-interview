#!/usr/bin/python3
"""module to find a winner for prime game"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game for a given set of rounds.
    """
    def sieve_of_eratosthenes(n):
        """
        Generate prime numbers up to n using the
        Sieve of Eratosthenes algorithm.
        """
        primes = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if primes[p] is True:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        # Count the primes after the sieve is constructed
        count = 0
        for p in range(2, n + 1):
            if primes[p]:
                count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        if primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
