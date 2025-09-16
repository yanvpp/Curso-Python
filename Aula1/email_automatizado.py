import pyautogui
import time

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa
    # abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=860, y=588)

    # digitar o site
time.sleep(0.5)
pyautogui.write("mail.google.com")
pyautogui.press("enter")

    #enviar o email
time.sleep(10)
pyautogui.click(x=142, y=215)
time.sleep(5)
pyautogui.write("Pai")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("teste automatizado")
pyautogui.press("tab")
pyautogui.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
time.sleep(7)
pyautogui.click(x=1302, y=1010)