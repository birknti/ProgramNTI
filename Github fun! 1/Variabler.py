import time


u = int(input("Vilken ålder är du? "))
u1 = input("Vad heter du? ")
u2 = float(input("Hur lång är du i meter? "))
u3 = float(input("Vad är det favorit number? "))

u4 = int(16)
u5 = "Birk"
u6 = float(1.9)
u7 = int(420)


print(f"Hej! {u1}, jag heter {u5}.")

time.sleep(3)

if u > u4:
    u9 = (u - u4)
    print(f"Du är äldre än mig med {u9} år. Jag är {u4} och du är {u}")

elif u < u4:
    u8 = (u4 - u)
    print(f"Du är yngre än mig med {u8} år. JAg är {u4} och du är {u}")

else:
    print("Vi är lika gamla.")


time.sleep(4)

print(f"du är {u2} meter lång och jag är {u6} meter lång. En {u6 - u2} meter längd skillnad.")

time.sleep(5)

if u3 == u7:

  print("Vi har samma favorit number!")

else:
  print(f"Vi har inte samma favorit number. Mitt är inte {u7}")