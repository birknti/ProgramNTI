import random
import time

while True:
 play = input("input (X/x) om du vill kasta din tärning: ")
 if play.lower() == "x":
    for spinner in range(10):
        x = random.randint(1, 6)
        print(f" tärning1\r{x}", end="", flush=True)
        time.sleep(0.15)

    print()

    for spinner in range(10):
        y = random.randint(1, 6)
        print(f" tärning2\r{y}", end="", flush=True)
        time.sleep(0.15)

    print()

    print(f"Du kasta {y + x}")
    continue
 else:
    continue
 