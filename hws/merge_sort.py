#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from numbers import Real


def merge(left: List[Real], right: List[Real]) -> List[Real]:
    """
    Merge two sorted lists of real numbers into one sorted list.

    >>> merge([1], [2]) == [1, 2]
    True

    >>> merge([1, 3, 5, 7], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    True

    >>> merge([1, 2, 3], []) == [1, 2, 3]
    True
    """

    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(array: List[Real]) -> List[Real]:
    """
    Sort the list of real numbers using merge sort.
    https://en.wikipedia.org/wiki/Merge_sort

    >>> merge_sort([3, 2, 1]) == [1, 2, 3]
    True

    >>> merge_sort(list(range(100, -1, -1))) == list(range(101))
    True

    >>> merge_sort([42]) == [42]
    True
    """

    result = array.copy()
    cur_size = 1

    while cur_size < len(result):
        left = 0

        while left < len(result):
            mid = min(left + cur_size, len(result))
            right = min(2 * cur_size + left, len(result))

            result[left:right] = merge(result[left:mid], result[mid:right])

            left = left + 2 * cur_size

        cur_size *= 2

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
