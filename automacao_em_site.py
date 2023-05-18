import pyautogui
from time import sleep
import webbrowser
import pyperclip


def escrever_nome(nome):
    pyperclip.copy(nome)
    pyautogui.hotkey('ctrl', 'v')


# Passo 1
# Navegar até o site
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(2)

# Passo 2
# Clicar no site e encontar o campo "exemplos alertas"
pyautogui.click(1520, 572, duration=2)
pyautogui.scroll(-1000)
sleep(1)

# Passo 3
# Clicar e digitar seu nome em "digite seu nome"
pyautogui.click(1749, 364, duration=2)
escrever_nome('Junior Rodrigues')
sleep(1)

# Passo 4
# Clicar no botão "alerta"
pyautogui.click(1731, 401, duration=2)
sleep(1)

# Passo 5 
# Clicar no botão "ok"
pyautogui.click(1639, 180, duration=2)
sleep(1)

# Passo 6
# Subir a página para cima novamente
pyautogui.scroll(1000)
sleep(1)

# Passo 7
# Descer até o tópico de donwloads
pyautogui.click()
pyautogui.scroll(-2700)
sleep(1)

# Passo 8
# Clicar em "fazer download" planilha excel e pdf
pyautogui.click(1186, 217, duration=2)
sleep(1)
pyautogui.click(1370, 192, duration=2)
sleep(1)

# Passo 9
# Criar um alerta de termino do programa
pyautogui.alert(text='Você terminou!', title='Fim do programa', button='OK')