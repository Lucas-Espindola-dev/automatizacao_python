import pyautogui
from time import sleep

pyautogui.click(803,453, duration=2)
pyautogui.write('user')
pyautogui.click(798,479, duration=1)
pyautogui.write('123456')
pyautogui.click(704, 509, duration=1)

with open('produtos.txt', 'r') as file:
    for linha in file:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(852, 385, duration=1)
        pyautogui.write(produto)
        pyautogui.click(839, 414, duration=0.3)
        pyautogui.write(quantidade)
        pyautogui.click(839, 443, duration=0.3)
        pyautogui.write(preco)
        pyautogui.click(752, 601, duration=0.5)
