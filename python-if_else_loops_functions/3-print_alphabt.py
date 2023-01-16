#!/usr/bin/python3
res = ""
for i in range(97, 123):
    if i != 101 and i != 113:
        res = res + chr(i)
print("{}".format(res), end="")
