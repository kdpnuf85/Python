"""
Print all two-letter combinations
Ported 11/19/2018
"""

x = 65
y = 91
combos = (y - x) ** 3
for a in range(x, y):
    for b in range(x, y):
        for c in range(x, y):
            print(chr(a) + chr(b) + chr(c),end = " ")
        print(" ")
    print(" ")

print("")
print(str(combos) + " possible combinations")
