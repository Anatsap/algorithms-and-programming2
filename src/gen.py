import random
n = 40
r = []
for i in range(n):
    s = []
    for j in range(n):
        s.append("N" if random.random() > 0.2 else "Y")
    r.append("".join(s))

with open("input.txt", "w") as f:
    f.write(f"{n} {n}\n")
    f.write(" ".join(r))