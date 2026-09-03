import time
while True:

 restart_program = False

 while True:
   _temp = input("Do you already have an account?(Y/n)")
   if _temp in ("N", "n"):
       del _temp
       correct_username = input("create username: ")
       correct_password = input("create password: ")
       break
   if _temp in ("Y", "y"):
       del _temp
       break
   print("You did not answer correctly")

 while True:
    username = input("enter your username: ")
    try: 
     username == correct_username
    except NameError:
            print("Account not found!")
            restart_program = True
            if restart_program == True:
               continue
    if username == correct_username:
     break      
    
    else:
     print("Account not found!")
 while True:
    for attempt in range(3):
        attempts_left = 3 - (attempt + 1)
        password = input(f"(You have {attempts_left+1} attempt(s) left)enter your password: ")
        if password == correct_password:
            print("logged in!")
            break
    if password == correct_password:
        break

    if attempts_left == 0:
        for seconds_left in range(5, 0, -1):
            print("Wait")
            print(seconds_left)
            time.sleep(1)
        continue

    break
 if restart_program == True:
    continue
 break