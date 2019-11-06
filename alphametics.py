import itertools
# Words are stored in reverse order to simplify this.
def val(solution, word):
    return sum(solution[l]*10**i for i, l in enumerate(word))

def solve(puzzle):
    numbers, sum_ = puzzle.split(" == ")
    sum_ = sum_[::-1]  # See comment above
    numbers = [num.strip()[::-1] for num in numbers.split("+")]
    # Initial letters are non-zero. Store them at the end of the list for speed.
    initials = set(w[-1] for w in numbers + [sum_])
    letters = list(set(filter(str.isalpha, puzzle)) - initials)+list(initials)

    for c in itertools.permutations(range(0,10), len(letters)):
        if 0 in c[-len(initials):]:  # Skip bad substitutions (initial letter is 0)
            continue
        solution = dict(zip(letters, c))
        if sum(val(solution, word) for word in numbers) == val(solution, sum_):
            return solution

    return {}