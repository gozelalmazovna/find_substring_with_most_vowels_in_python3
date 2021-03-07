import math
import os
import random
import re
import sys

def findSubstring(s, k):
    """
    The 'findSubstring' function below, finds substring of the given string s
    with the most number of vowels.
    It will return substring with smallest index position
    The function returns a STRING.
    The function accepts following parameters:
    1. STRING s
    2. INTEGER k (substring length)
    """
    a = k  #I want to preserve k
    vowel_counted = {} #dictionary with all the possible substrings
    i = 0
    while i <= len(s):
        if len(s[i:k]) == a: 
            my_str = s[i:k]
            total_num = 0
            for vowel in "aeiou":
                count = my_str.count(vowel)
                total_num += count
            vowel_counted[my_str] = total_num
        i += 1
        k += 1

    val_key = str()
    for key in vowel_counted.keys():
        if val_key == "":
            val_key = key
        if vowel_counted[val_key] != vowel_counted[key] and vowel_counted[val_key] < vowel_counted[key] :
            val_key = key

    if len(val_key) != 0:
        return val_key

    else:
        return "Not found!"

print(findSubstring("leambsdsfaeoim", 5))
