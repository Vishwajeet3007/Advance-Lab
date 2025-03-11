from collections import Counter
def UniqueNumber(arr):
    freq  = Counter(arr)
    for i , ch in enumerate(arr):
        if freq[ch] == 1:
            return ch
    return -1
# Test cases
arr = [2,4,7,4,2]
print(UniqueNumber(arr))