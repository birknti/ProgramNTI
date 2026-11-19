import msvcrt
import os

påse = []
spel = True

while spel:
    print("Dina Val för din påse!\n")
    print("[V] Visa innehållet i påsen\n[S] Spara i påsen\n[F] Leta (finns) i påsen\n[Q] Avsluta programmet\n\n")
    svar = input("Ditt val: ")

    if svar.lower() == "v":
        os.system("cls")
        print(f"Här är vad du har i din påse!\n\n{påse}\n\nTryck på valfri tangent för att fortsätta.")
        msvcrt.getch()
        os.system("cls")
    
    elif svar.lower() == "s":
        os.system("cls")
        x = input("Vad vill du lägga till?: ")
        påse.append(x.lower())
        print(f"\n ({x}) Har lagts till i din påse!\n\n Tryck på valfri tangent för att fortsätta.")
        msvcrt.getch()
        os.system("cls")
    
    elif svar.lower() == "f":
        os.system("cls")
        x = input("Vad letar du efter i påsen?: ")
        if x.lower() in påse:
            print(f"({x}) Hittades i din påse!\n\n Tryck på valfri tangent för att fortsätta.")
            msvcrt.getch()
            os.system("cls")

    elif svar.lower() == "q":
        os.system("cls")
        print("Välkommen åter till din påse!")
        spel = False

    else:
        print("Enter one of the letters in the brackets instead.")


        