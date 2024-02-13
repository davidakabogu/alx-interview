def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def determine_winner(nums):
    prime_count = sum(is_prime(i) for i in range(1, max(nums) + 1))
    return "Maria" if prime_count % 2 == 1 else "Ben"


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = determine_winner(range(1, n + 1))
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
