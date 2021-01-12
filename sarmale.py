import sys
import pyautogui
import time
import keyboard

def orderShaorma(nrTelfon, emailProfil, parolaProfil, adresaComanda, andresaMore, verbose):
    pyautogui.click(87, 1050); time.sleep(0.5)
    pyautogui.click()  
    keyboard.write("chrome")
    keyboard.press("enter")
    if verbose: print("opening chrome...")
    time.sleep(0.5)
    keyboard.write("https://glovoapp.com/")
    if verbose: print("going to glovo...")
    time.sleep(0.5)
    keyboard.press("enter"); time.sleep(5)
    pyautogui.click(1460, 730); time.sleep(1)
    pyautogui.click(1605, 745); time.sleep(1)
    pyautogui.click(1633, 600); time.sleep(1)
    if verbose: print("searching order place...")
    keyboard.write("German Doner Kebab"); time.sleep(2)
    pyautogui.click(460, 980); time.sleep(1)
    pyautogui.scroll(-250); time.sleep(1)
    pyautogui.click(); time.sleep(1)
    if verbose: print("buyng shaorma")
    pyautogui.scroll(-500); time.sleep(1)
    pyautogui.click(930, 930); time.sleep(1)
    pyautogui.scroll(-200); time.sleep(1)
    pyautogui.click(1420, 870); time.sleep(1)
    pyautogui.scroll(200); time.sleep(1)
    pyautogui.click(1420, 960); time.sleep(1)
    pyautogui.click(1030, 850); time.sleep(1)
    pyautogui.click(780, 390); time.sleep(1)
    keyboard.write(emailProfil); time.sleep(0.5)
    pyautogui.click(780, 515); time.sleep(1)
    keyboard.write(parolaProfil); time.sleep(0.5)
    pyautogui.click(1015, 650); time.sleep(1)
    pyautogui.click(630, 430); time.sleep(1)
    keyboard.write(adresaComanda); time.sleep(3)
    pyautogui.click(630, 500); time.sleep(1)
    pyautogui.click(600, 560); time.sleep(1)
    keyboard.write(andresaMore); time.sleep(3)
    pyautogui.click(960, 870); time.sleep(1)
    pyautogui.scroll(-750)
    pyautogui.click(550, 530)
    pyautogui.click(470, 640)
    pyautogui.scroll(-350); time.sleep(0.5)
    pyautogui.click(515, 690); time.sleep(0.5)
    pyautogui.click(900, 480)
    keyboard.write(nrTelfon); time.sleep(0.5)
    pyautogui.click(960, 740); time.sleep(15)
    pyautogui.scroll(-350); time.sleep(0.5)
    pyautogui.click(960, 950)

def compile(name, verbose):
    nrTelfon = ""
    emailProfil = ""
    parolaProfil = ""
    adresaComanda = ""
    andresaMore = ""
    if verbose:
        print("opening file: " + name)
    order = False
    f = open(name, "r")
    for line in f:
        value = ""
        varabila = ""
        if line == "order shaorma":
            order = True
            if(verbose): print("starting to order shaorma")
        elif "var." in line:
            value = line[line.index('=')+2:len(line)-1]
            varabila = line[line.index('.')+1:line.index(' ')]
        if verbose: print(varabila + " : " + value)
        if varabila == 'tel': nrTelfon = value
        elif varabila == 'email': emailProfil = value
        elif varabila == 'parola': parolaProfil = value
        elif varabila == 'adr1': adresaComanda = value
        elif varabila == 'adr2': andresaMore = value
    if order:
        orderShaorma(nrTelfon, emailProfil, parolaProfil, adresaComanda, andresaMore, verbose)
        
if __name__ == '__main__':
    nrArgumente = len(sys.argv)-1
    if nrArgumente == 0:
        print("sarmale: not enough arguments")
        print("usage: sarmale [options] [filename]")
        print("optinons:")
        print("    -help: shows you how sarmale works")
        print("    -v,verbose: debug while compiling")
        exit(0)

    if sys.argv[1] == '-help':
        print("usage: sarmale [options] [filename]")
        print("optinons:")
        print("    -help: shows you how sarmale works")
        print("    -v,verbose: debug while compiling")
        exit(0)

    exista = False
    verbose = False
    pozitie = 0
    for i in range(1, len(sys.argv)):
        if ".nu" in sys.argv[i]:
            pozitie = i
            exista = True
            if verbose:
                print("compiling file: " + sys.argv[i])
        if sys.argv[i] == '-v' or sys.argv[i] == '-verbose':
            verbose = True
            print("verbose turned on")
    if exista:
        print("DO NOT TOUCH YOU KEYBOARD OR MOUSE WHILE IT IS RUNNING")
        print("IF SOMETHING GOES WRONG PRESS CTRL+C FROM THE CONSOLE")
        time.sleep(3)
        compile(sys.argv[pozitie], verbose)

