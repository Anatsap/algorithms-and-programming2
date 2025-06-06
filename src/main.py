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
if __name__ == "__main__":
    haystack = "bcbcaabaabcbcbb"
    needle = "bcb"

    res = search(needle, haystack)
    for i in range(len(res)):
        print(res[i], end=" ")
