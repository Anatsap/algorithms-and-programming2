import random

num_patterns = 10
pattern_length = 6

patterns = []
for _ in range(num_patterns):
    pattern = ''.join("0" if random.random() > 0.3 else "1" for _ in range(pattern_length))
    patterns.append(pattern)

with open("needle.txt", "w") as f:
    f.write(" ".join(patterns))
