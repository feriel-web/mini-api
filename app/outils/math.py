
def factorielle(n: int) -> int:
    if n < 0:
        raise ValueError("n doit être positif ou nul")

    return 1 if n <= 1 else n * factorielle(n - 1)
