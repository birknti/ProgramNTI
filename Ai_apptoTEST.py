import random
import tkinter as tk


def spin():
    spin_button.config(state="disabled")
    result.config(text="Spinning...")
    steps = 0

    def update_numbers():
        nonlocal steps

        x = random.randint(1, 9)
        y = random.randint(1, 9)
        z = random.randint(1, 9)

        num1.config(text=str(x))
        num2.config(text=str(y))
        num3.config(text=str(z))

        steps += 1

        if steps < 15:
            window.after(80, update_numbers)
        else:
            if x == y == z:
                result.config(text="You win!")
            else:
                result.config(text="Try again!")

            spin_button.config(state="normal")

    update_numbers()


window = tk.Tk()
window.title("Lucky Numbers")
window.geometry("300x220")

title = tk.Label(window, text="Spin the numbers", font=("Arial", 16))
title.pack(pady=10)

frame = tk.Frame(window)
frame.pack()

num1 = tk.Label(frame, text="0", font=("Arial", 24), width=3)
num1.grid(row=0, column=0, padx=10)

num2 = tk.Label(frame, text="0", font=("Arial", 24), width=3)
num2.grid(row=0, column=1, padx=10)

num3 = tk.Label(frame, text="0", font=("Arial", 24), width=3)
num3.grid(row=0, column=2, padx=10)

spin_button = tk.Button(window, text="Spin", font=("Arial", 12), command=spin)
spin_button.pack(pady=15)

result = tk.Label(window, text="Ready!", font=("Arial", 12))
result.pack()

window.mainloop()