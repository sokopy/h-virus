import os, sys, time, random
os.system("color 1 & title H virus safe [version 1] & cls")
l = list("ħhɦɥʜĥḧḩȟɧʮʯℋℌℍℎℏ♄♅🄗🄷🅷Ⓗ🅗🇭ĦHꞪꞍʜĤḦḨȞ")
print(">>>>>>>>>>>>>>>> The safe H virus (version 1) <<<<<<<<<<<<<<<<\n")
while True:
    confirm = input("Do you want to execute the safe version of the H virus? I am not responsible for software damage or other consequences\n(y/n) ")
    if confirm == "n":
        print("Closing program...")
        time.sleep(1)
        sys.exit()
    elif confirm == "y":
        break
    else:
        print("Invalid input. Type \"y\" to proceed or \"n\" to cancel")
        time.sleep(2)
        os.system("cls")
text = ""
title = ""

for i in range(50):
    for i in range(50):
        title += l[random.randint(0, len(l)-1)]
    with open(title, "a", encoding="utf-8") as file:
        for i in range(200):
            text += l[random.randint(0, len(l)-1)]
        file.write(text)
        text = ""
        title = ""