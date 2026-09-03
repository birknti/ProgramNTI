import tkinter as tk

def Sign_up():
    global created_username, created_password
    created_username = username.get()
    created_password = password.get()
    print(created_username, created_password)
    
def Sign_in():
    if usernamee.get() == created_username:
        if passworde.get() == created_password:
            print("Signed in")
        else:
            print("Wrong password.")
    else:
        print("User not found.")

window = tk.Tk()
window.title("Login window")
window.geometry("550x300")

username = tk.Entry(window)
username.pack()

password = tk.Entry(window)
password.pack()

button = tk.Button(window, text="Signup", command=Sign_up)
button.pack()

usernamee = tk.Entry(window)
usernamee.pack()

passworde = tk.Entry(window)
passworde.pack()

button = tk.Button(window, text="Signin", command=Sign_in)
button.pack()


window.mainloop()