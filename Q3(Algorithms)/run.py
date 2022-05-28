from collections import Counter

array = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5]    # the below function works with any number of elements


def get_duplicate():
    """

    :rtype: the first duplicated object on the array
    """
    c = Counter()
    seen = set()
    for i in array:
        c[i] += 1
        if c[i] > 1 and i not in seen:
            seen.add(i)
            return i


print(get_duplicate())
