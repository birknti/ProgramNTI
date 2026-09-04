import time

correct_password = "yolo_swag"
while True:

  while True:
    for attempt in range(3):
        attempts_left = 3 - (attempt + 1)
        password = input(f"(You have {attempts_left+1} attempt(s) left)enter the password: ")
        if password == correct_password:
            print("Welcome to swag world.")
            break
    if password == correct_password:
        break

    if attempts_left == 0:
        for seconds_left in range(10, 0, -1):
            print(f"  wait, if you want to enter swag world.\r{seconds_left}", end="", flush=True)
            time.sleep(1)

        print()
        continue

    continue
 