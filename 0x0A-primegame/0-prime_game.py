#!/usr/bin/python3
"""Prime Game"""


def isPrime(n):
    # 0, 1, and even numbers greater than 2 are NOT PRIME
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        # Check divisibility up to the square root of n
        # Start from 3 and iterate over odd numbers only
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


def isRoundWinner(n, x):
    """find round winner"""
    list = [i for i in range(1, n + 1)]
    players = ["Maria", "Ben"]

    for i in range(n):
        # get current player
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(list):
            # if already picked prime num then
            # find if num is multipl of the prime num
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            # else check is num is prime then pick it
            else:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num
        # if failed to pick then current player lost
        if prime == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selectedIdxs):
                del list[val - idx]
    return None


def isWinner(x, nums):
    """finds the winner"""
    winnerCounter = {"Maria": 0, "Ben": 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter["Maria"] > winnerCounter["Ben"]:
        return "Maria"
    elif winnerCounter["Ben"] > winnerCounter["Maria"]:
        return "Ben"
    else:
        return None
