import os
import time
from itertools import zip_longest as zip


def buildlps(needle, lps):
    len1 = 0
    m = len(needle)
    lps[0] = 0

    i = 1
    while i < m:
        if needle[i] == needle[len1]:
            len1 += 1
            lps[i] = len1
            i += 1
        else:
            if len1 != 0:
                len1 = lps[len1 - 1]
            else:
                lps[i] = 0
                i += 1


def search(needle, haystack):
    n = len(haystack)
    m = len(needle)

    lps = [0] * m
    res = []
    buildlps(needle, lps)
    i = 0
    j = 0
    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                res.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res
def result(needle, haystack):
    return search(needle, haystack)

if __name__ == "__main__":
    file_path = "haystack.txt"
    if os.stat(file_path).st_size == 0:
        print("File is empty, you can not search ")
    else:
        with open("needle.txt") as textfile1, open("haystack.txt") as textfile2:
            for x, y in zip(textfile1, textfile2):
                needle = x.strip()
                haystack = y.strip()
                print(f"{needle}\t{haystack}")
                result = result(needle, haystack)
                print(result)

                new_file = "new_file.txt"
                with open(new_file, 'w') as file:
                    file.write("Hello, this is a test.")
                print(f"File '{new_file}' created successfully.")

