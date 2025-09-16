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
pyautogui.write("destinatário") # altere com o endereço de email do destinatário
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("assunto") # altere com o assunto do email
pyautogui.press("tab")
pyautogui.write("mensagem") # adicione o corpo da mensagem
time.sleep(7)
pyautogui.click(x=1302, y=1010)