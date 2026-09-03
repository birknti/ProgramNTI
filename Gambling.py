import random
import time
import tkinter as tk

def Spin():

    for spinner in range(10):
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        z = random.randint(1, 9)
        print(f"\r{x} {y} {z}", end="", flush=True)
        time.sleep(0.15)

    print()

    if x == y == z:
        print("You win!")

window = tk.Tk()
window.title("Gamble")
window.geometry("550x300")

button = tk.Button(window, text="Spin", command=Spin)
button.pack()

