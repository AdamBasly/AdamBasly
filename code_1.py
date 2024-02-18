print("Hello in this KI. Please select your language. (English is under develepoment)")
print("German (Deutsch) (1)")
print("English (2)")
print("evaluate (1/2)")
language=int(input("Please integer:"))
if language==1:
    print("Du hast Deutsch ausgewählt")
    eingabe=input("Was willst du tun?")
    while True:
        if eingabe=="help" or eingabe=="hilfe":
            print("1=lernen mit der Maus. 2=mehr über dich")
            abfrage1=input("Willst du die KI abbrechen?")
            if abfrage1=="Ja":
                break
        elif eingabe=="1":
            learn=input("Was willst du genau lernen?")
            if learn=="Python":
                print("https://www.udemy.com/")
                abfrage2=input("Willst du di KI abbrechen?")
                if abfrage2=="Ja":
                    break
        elif eingabe=="2":
            print("Ich bin die KI von adamrun155")
        elif eingabe=="Github"or eingabe=="github":
            print("https://github.com/")
        elif eingabe=="Visual Studio Code" or eingabe=="visual studio code" or eingabe=="install coding application":
            print("https://code.visualstudio.com/")
        elif eingabe=="eat something" or "etwas essen":
            print("https://mama-pizza.de/")
        eingabe=input("Was willst du jetzt tun?")
elif language==2:
    print("You have choosed English")
    eingabe=input("What do you want to do")
    while True:
        if eingabe=="help" or eingabe=="hilfe":
            print("1=learn with the mouse. 2=more about you")
            abfrage1=input("Do you want to abort the KI?")
            if abfrage1=="Yes":
                break
        elif eingabe=="1":
            learn=input("What do you want to learn?")
            if learn=="Python":
                print("https://www.udemy.com/")
                abfrage2=input("Do you want to abort the KI?")
                if abfrage2=="Ja":
                    break
        elif eingabe=="2":
            print("I'm the KI of adamrun155")
        elif eingabe=="Github"or eingabe=="github":
            print("https://github.com/")
        elif eingabe=="Visual Studio Code" or eingabe=="visual studio code" or eingabe=="install coding application":
            print("https://code.visualstudio.com/")
        elif eingabe=="eat something" or "etwas essen":
            print("https://mama-pizza.de/")
        eingabe=input("What do you want to do?")
print("Du hast die KI abgebrochen./You have aborted the KI.")
