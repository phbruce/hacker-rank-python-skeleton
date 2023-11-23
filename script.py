#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'playingWithNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def playingWithNumbers(arr, queries):
    matrix = []

    def sum_abs(arr):
        return sum([abs(i) for i in arr])

    def sum_item(agg, arr, query):
        return [agg.append(a + query) for a in arr]

    for idx, query in enumerate(queries):
        agg = []

        if idx == 0:
            sum_item(agg, arr, query)
            matrix.append(agg)
        else:
            new_arr = matrix[idx-1]
            sum_item(agg, new_arr, query)
            matrix.append(agg)

    return [sum_abs(agg) for agg in matrix]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    queries = list(map(int, input().rstrip().split()))

    result = playingWithNumbers(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
