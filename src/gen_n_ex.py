import random
r = []
for i in range(4):
    s = []
    for j in range(5):
        s.append("0" if random.random() > 0.3 else "1")
    r.append("".join(s))

with open("needle.txt", "w") as f:
    f.write(" ".join(r))