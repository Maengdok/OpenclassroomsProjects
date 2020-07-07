import random, string
rand = "".join([random.choice(string.printable) for _ in range(24)])
print("\"{}\"".format(rand))
