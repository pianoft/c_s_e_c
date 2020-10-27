from base64 import *
import uu


def f(s):
    return b64decode(s)


p1 = open("e.txt", 'r').read()
for i in range(0, 16):
    p1 = f(p1)
    print(p1)

p2 = open("in.txt", 'a')
p2.write(p1.decode())
p2.close()

uu.decode('in.txt', 'out.txt')
print("")
print(open('out.txt', 'r').read())
