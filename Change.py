from typing import List

Change = List[int]


def find_fewest_coins(coins: Change, total: int) -> Change:
    """
    Find the fewest coins required to produce a given total.
    """
    if total < 0:
        raise ValueError("Value for total cannot be negative!")
    stop = total + 1
    number_required = [0] + [stop] * total
    denominations_used = [stop] + [0] * total
    for denomination in range(1, stop):
        min_required = number_required[denomination]
        for coin in (c for c in coins if c <= denomination):
            delta = denomination - coin
            current_required = number_required[delta] + 1
            if current_required < min_required:
                min_required = current_required
                denominations_used[denomination] = delta
        number_required[denomination] = min_required

    # we may have gotten to a no solution outcome
    if number_required[total] == stop:
        raise ValueError("Cannot make exact change with coins provided!")

    coin_used = total
    result = []
    while denominations_used[coin_used] != stop:
        result.append(coin_used - denominations_used[coin_used])
        coin_used = denominations_used[coin_used]
    return result
