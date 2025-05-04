import random
n = 40
r = []
for i in range(n):
    s = []
    s.append("0" if random.random() > 0.3 else "1")
    r.append("".join(s))

with open("haystack.txt", "w") as f:
    f.write("".join(r))